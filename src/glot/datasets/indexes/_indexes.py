import importlib.resources
import json


NAME_INDEX_MAP_PATH = importlib.resources.files("glot.datasets.indexes").joinpath("indexes.json")

def name_index_map() -> dict[str, str]:
    with NAME_INDEX_MAP_PATH.open("r") as fp:
        return json.load(fp)


def _get(name: str):
    try:
        return name_index_map()[name]
    except KeyError:
        raise ValueError(
            f"Dataset `name` '{name}' not found in `glot.dataset.indexes._indexes.name_index_map`. "
            f"Valid values for `name` are: {list(name_index_map().keys())}"
        )


def _update_indexes_json(dataset_name: str, index_json_name: str):
    with NAME_INDEX_MAP_PATH.open("r") as fp:
        indexes_json = json.load(fp)
    indexes_json[dataset_name] = index_json_name
    with NAME_INDEX_MAP_PATH.open("w") as fp:
        json.dump(indexes_json, indent=4)
