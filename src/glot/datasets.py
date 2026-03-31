"""module that loads dataset names,
so that user can see what datasets are available.
"""
import json
from pathlib import Path

import yaml


HERE = Path(__file__).parent
DATASETS_YAML = HERE.joinpath('datasets.yaml')
with DATASETS_YAML.open() as f:
    dataset_dict = yaml.safe_load(f)

dataset_names = [k for k in dataset_dict.keys()]


def show():
    print(json.dumps(dataset_dict, indent=1))
