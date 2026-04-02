import importlib.resources
import json


NAME_INDEX_MAP_PATH = importlib.resources.files("glot.datasets.indexes") / "indexes.json"
with NAME_INDEX_MAP_PATH.open("r") as fp:
    NAME_INDEX_MAP = json.load(fp)


def _get(name: str):
    try:
        return NAME_INDEX_MAP[name]
    except KeyError:
        raise ValueError(
            f"Dataset `name` '{name}' not found in `glot.indexes.NAME_INDEX_MAP`. "
            f"Valid values for `name` are: {NAME_INDEX_MAP.keys()}"
        )


def _update_indexes_json(dataset_name: str, index_json_name: str):
    with open("src/glot/datasets/indexes/indexes.json", "r") as fp:
        indexes_json = json.load(fp)
    indexes_json[dataset_name] = index_json_name
    with open("src/glot/datasets/indexes/indexes.json", "w") as fp:
        json.dump(indexes_json, indent=4)
