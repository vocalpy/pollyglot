"""script that generates the Pollyglot data repository"""
import argparse
from pathlib import Path
import shutil
import tarfile
import urllib.request

import yaml

HERE = Path(__file__).parent
REPO_YAML = HERE.joinpath('../../data/repo.yaml')
with REPO_YAML.open() as f:
    repo_dict = yaml.safe_load(f)

repo_keys = [k for k in repo_dict.keys()]

# target paths
DOWNLOADS_DIR = HERE.joinpath('../../results/downloads')
TARGZBALLS_DIR = HERE.joinpath('../../results/targzballs')


def clean():
    downloads_dir_dirs = DOWNLOADS_DIR.glob('/*/')
    shutil.rmtree(downloads_dir_dirs)

    targzballs_dir_dirs = TARGZBALLS_DIR.glob('/*/')
    shutil.rmtree(targzballs_dir_dirs)


def make_download_dirs():
    for repo_key in repo_keys:
        download_dir = DOWNLOADS_DIR / f"{repo_key}"
        download_dir.mkdir()


def download():
    for repo_key, repo_url_dict in repo_dict.items():
        local_repo_path = DOWNLOADS_DIR.joinpath(repo_key)
        if 'data_url' in repo_url_dict:
            data_url = repo_url_dict['data_url']
            local_filename, headers = urllib.request.urlretrieve(
                url=data_url, filename=local_repo_path
            )
        tar = tarfile.open(local_filename)
        tar.extractall()


def targzball():
    for repo_key in repo_keys:
        results_tar_gz = TARGZBALLS_DIR / f'{repo_key}.tar.gz'


def all():
    make_download_dirs()
    download()
    targzball()


def make(command):
    """a function that acts kind of like Unix make
    except that you don't have to do backflips to get it
    to work on a whole directory
    """
    if command == 'clean':
        clean()
    elif command == 'all':
        all()


def get_argparser():
    DESCRIPTION = 'command-line interface for script that generates Pollyglot dataset'
    CHOICES = [
        'clean',
        'all',
        'make_downloads_dirs',
        'download',
        'targzball',
    ]

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('command', type=str, metavar='command',
                        choices=CHOICES,
                        help="Command to run, valid options are:\n"
                             f"{CHOICES}\n"
                             "$ vak train ./configs/config_2018-12-17.ini")
    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()
    make(args.command)


if __name__ == '__main__':
    main()
