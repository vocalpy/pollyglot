import argparse
import json

import pooch
import vocalpy as voc
import tqdm

import glot
from glot.typing import PathLike


REPO_STRUCTURE = {
    "bl26lb16": [
        "041912",
        "042012",
        "042112",
    ],
    "gr41rd51": [
        "061912",
        "062012",
        "062112",
        "062212",
        "062312",
    ],
    "gy6or6": [
        "032212",
        "032312",    
        "032412",
        "032512",
        "032612",
    ],
    "or60yw70": [
        "092712",
        "092812",
        "092912",
        "093012",
        "100112",
    ]
}


INDEX_DST_PATH = glot.constants.INDEXES_ROOT / "bfsongrepo.json"


def make_index(
    root: PathLike,# FIXME: what is current BFSongRepo version?
    dry_run: bool = True,
) -> None:
    root = glot.validators.validate_root(root)

    print(
        f"Making index from root: {root}"
    )

    index = {
        "version": "9.0.0",
        "items": [],
    }

    to_make_all_subdirs = []
    for bird_id, subdirs in REPO_STRUCTURE.items():
        for subdir_name in subdirs:
            to_make_all_subdirs.append(
                (bird_id, subdir_name)
            )

    all_subdirs = []
    pbar = tqdm.tqdm(to_make_all_subdirs)
    for bird_id, subdir_name in pbar:
        bird_id_root = root / bird_id
        if not bird_id_root.exists() or not bird_id_root.is_dir():
            raise NotADirectoryError(
                f"Expected directory for `bird_id` '{bird_id}' "
                f"not found in `root`: {bird_id_root}"
            )
        subdir_path = bird_id_root / subdir_name
        if not subdir_path.exists() or not subdir_path.is_dir():
            raise NotADirectoryError(
                f"Expected sub-directory for `bird_id` '{bird_id}' "
                f"not found: {subdir_path}"
            )
        pbar.set_description(
            f"Adding sub-directory: {bird_id}/{subdir_name}"
        )
        all_subdirs.append((bird_id, subdir_path))

    pbar = tqdm.tqdm(all_subdirs)
    for bird_id, subdir in pbar:
        pbar.set_description(f"Making items from sub-dir: {subdir.name}")
        wavs_this_subdir = voc.paths.from_dir(subdir, "wav")
        if len(wavs_this_subdir) == 0:
            raise FileNotFoundError(
                f"No wav files found for sub-directory: {subdir}"
            )
        # not all wavs have corresponding csv annotation files;
        # specifically gr41rd51 does not have all files annotated.
        # so we check that there are greater than zero csv files,
        # but instead of using these, below when we iterate throuh wav files, 
        # we build the corresponding csv file name programatically
        # and only include it if the file actually exists
        csvs_this_subdir = voc.paths.from_dir(subdir, "csv")
        if len(csvs_this_subdir) == 0:
            raise FileNotFoundError(
                f"No csv files found for sub-directory: {subdir}"
            )

        wavs_pbar = tqdm.tqdm(wavs_this_subdir)
        for wav_path in wavs_pbar:
            csv_path = wav_path.parent / (wav_path.name + ".csv")
            if not csv_path.exists():
                csv_path = None
            item = {
                "id": wav_path.stem,
                "sound": {
                    "path": str(wav_path.relative_to(root)),
                    "hash": pooch.file_hash(wav_path)
                },
                "annot": {
                    "path": str(csv_path.relative_to(root)) if csv_path is not None else csv_path,
                    "hash": pooch.file_hash(csv_path) if csv_path is not None else csv_path
                },
                "metadata": {
                    "bird_id": bird_id
                }
            }
            index["items"].append(item)

    print(
        f"Built index with {len(index["items"])} items"
    )
    if not dry_run:
        print(
            f"Saving index in {INDEX_DST_PATH}"
        )
        with INDEX_DST_PATH.open("w") as fp:
            json.dump(
                index, fp, indent=4
            )
        glot.datasets.indexes._indexes._update_indexes_json("BFSongRepo", INDEX_DST_PATH.name)


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "root",
        help="Path to root of dataset",
    )
    parser.add_argument(
        "--dry-run",
        action=argparse.BooleanOptionalAction,
        default=True,
    )
    args = parser.parse_args()
    return args


args = get_args()
make_index(
    args.root,
    args.dry_run,
)
