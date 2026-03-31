"""Bengalse Finch Song Repository dataset"""
from typing import Callable

import crowsetta
import pooch
import vocalpy as voc

from . import indexes
from ..item import Item
from ..typing import PathLike


BIBTEX = """
"""

LICENSE = ""

BASE_URL = "doi:10.6084/m9.figshare.4805749.v9"

BIRD_ID_TAR_GZ_MAP = {
    "bl26lb16": [
        'sober.repo1.gr41rd51.062312.wav.csv.tar.gz', 
        'sober.repo1.bl26lb16.042112.wav.csv.tar.gz', 
        'sober.repo1.bl26lb16.042012.wav.csv.tar.gz', 
        'sober.repo1.bl26lb16.041912.wav.csv.tar.gz',
    ],
    "gr41rd51": [
        'sober.repo1.gr41rd51.062112.wav.csv.tar.gz', 
        'sober.repo1.gr41rd51.062012.wav.csv.tar.gz', 
        'sober.repo1.gr41rd51.061912.wav.csv.tar.gz', 
        'sober.repo1.gr41rd51.062212.wav.csv.tar.gz', 
    ],
    "gy6or6": [
        'sober.repo1.gy6or6.032212.wav.csv.tar.gz', 
        'sober.repo1.gy6or6.032312.wav.csv.tar.gz', 
        'sober.repo1.gy6or6.032412.wav.csv.tar.gz', 
        'sober.repo1.gy6or6.032512.wav.csv.tar.gz', 
        'sober.repo1.gy6or6.032612.wav.csv.tar.gz', 
    ],
    "or60yw70": [
        'sober.repo1.or60yw70.092912.wav.csv.tar.gz', 
        'sober.repo1.or60yw70.100112.wav.csv.tar.gz', 
        'sober.repo1.or60yw70.092712.wav.csv.tar.gz', 
        'sober.repo1.or60yw70.092812.wav.csv.tar.gz', 
        'sober.repo1.or60yw70.093012.wav.csv.tar.gz', 
    ],
}


SCRIBE = crowsetta.Transcriber(format="simple-seq")
def annot_loader(annot_path: PathLike) -> crowsetta.Sequence:
    return SCRIBE.from_file(annot_path).to_seq()


class BFSongRepo:

    def __init__(
        self,
        root: PathLike,
        sound_transform: Callable | None = None,
        annot_transform: Callable | None = None,
        download: bool = False,
        sound_loader=voc.Sound.read,
        annot_loader=annot_loader,
    ):
        self.root = root
        self.sound_transform = sound_transform
        self.annot_transform = annot_transform
        self.sound_loader = sound_loader
        self.annot_loader = annot_loader

        if download:
            # FIXME: have docstring that shows you should *not* have multiple dirs for each bird ID
            self._pooch = pooch.create(path=root, base_url=BASE_URL, registry=None)
            self._pooch.load_registry_from_doi()
            for bird_id, tar_gz_list in BIRD_ID_TAR_GZ_MAP.items():
                for tar_gz_to_fetch in tar_gz_list:
                    self._pooch.fetch(tar_gz_to_fetch, processor=pooch.Untar)

        index = indexes.get("BFSongRepo")
        index["items"] = [
            item for item in index["items"]
            if item["metadata"]["bird_id"] in self.bird_ids
        ]
        self.index = index

    def __getitem__(self, idx) -> Item:
        idx_item = self.index["items"][idx]
        sound = self.sound_loader(idx_item["sound"]["path"])
        annot = self.annot_loader(idx_item["annotation"]["path"])
        if self.sound_transform is not None:
            sound = self.sound_transform
        if self.annot_transform is not None:
            annot = self.annot_transform
        return Item(
            sound=sound,
            annot=annot,
        )

    def __len__(self, idx):
        return len(self.index["items"])
