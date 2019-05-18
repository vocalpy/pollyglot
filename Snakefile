from pathlib import Path

data_path = Path('data')  # i.e. './data/'
data_dirs = list(data_path.glob('*/'))  # all child directories in data/

results_tar_gz = []
for data_dir in data_dirs:
    dirname = data_dir.parts[1]
    results_tar_gz.append(f'results/{dirname}.tar.gz')

rule all:
  input:
    results_tar_gz

rule clean:
  shell:
    "rm ./results/*.tar.gz"

rule compress:
  input:
    "data/{name}/"
  output:
    "results/{name}.tar.gz"
  shell:
    "tar -czvf {output} {input}"
