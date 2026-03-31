import pathlib

from glot.typing import PathLike


def validate_root(root: PathLike) -> pathlib.Path:
    root = pathlib.Path(root)
    if not root.exists() or not root.is_dir():
        raise NotADirectoryError(
            f"`root` not found or is not a directory: {root}"
        )
    return root

