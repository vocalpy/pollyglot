import dataclasses

import vocalpy as voc


@dataclasses.dataclass
class Item:
    """Class that represents an item in a dataset"""
    sound: voc.Sound
    annot: voc.Annotation | None = None

    def asdict(self):
        return dataclasses.asdict(self)