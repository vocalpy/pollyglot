import dataclasses

import vocalpy as voc


@dataclasses.dataclass
class Item:
    """A :class:`~dataclasses.dataclass` that represents an item in a :mod:`glot` dataset.
    
    Attributes
    ----------
    sound : vocalpy.Sound
    annot : vocalpy.Annotation

    Methods
    -------
    asdict
    """
    sound: voc.Sound
    annot: voc.Annotation | None = None

    def asdict(self):
        """Convert :class:`Item` to a :class:`dict`"""
        return dataclasses.asdict(self)