from pathlib import Path

import yaml

REPO_YAML = Path('data/repo.yaml')
with REPO_YAML.open() as f:
    repo_dict = yaml.safe_load(f)

repo_keys = [k for k in repo_dict.keys()]
results_tar_gz = [f"results/targzballs/{repo_key}.tar.gz" for repo_key in repo_keys]

rule all:
  input:
    results_tar_gz

rule clean:
  shell:
    "rm -rf ./results/downloads/*/",
    "rm ./results/targzballs/*.tar.gz"

rule make_downloads_dirs:
  input:
    repo_keys
  output:
    "results/downloads/{name}/"
  shell:
    "mkdir ./results/downloads/{input}"

rule download:
  input:
    "results/downloads/{name}/"
  output:
    "results/downloads/{name}/"
  run:
    for repo_key, repo_url_dict in repo_dict.items():
    

rule targzball:
  input:
    "results/downloads/{name}/"
  output:
    "results/targzballs/{name}.tar.gz"
  shell:
    "tar -czvf {output} {input}"
