"""script that generates the Pollyglot data repository"""
import argparse
import os
from pathlib import Path
import pkg_resources
import shutil
import tarfile
import zipfile

import rarfile

from .datasets import dataset_dict, dataset_names
from .urlcopy import urlcopy

HERE = Path(__file__).parent

# target paths
DOWNLOADS_DIR = HERE.joinpath('../../results/downloads')
TARGZBALLS_DIR = HERE.joinpath('../../results/targzballs')


tarprep_funcs = {}
for tarprep_func in pkg_resources.iter_entry_points(group='pollyglot.tarprep'):
    tarprep_funcs.update(
        {tarprep_func.name: tarprep_func.load()}
    )


def clean():
    downloads_dir_dirs = [d for d in DOWNLOADS_DIR.iterdir() if d.is_dir()]
    if downloads_dir_dirs:
        for downloads_dir in downloads_dir_dirs:
            shutil.rmtree(downloads_dir)

    targzballs_dir_dirs = [d for d in TARGZBALLS_DIR.iterdir() if d.is_dir()]
    if targzballs_dir_dirs:
        for targzballs_dir in targzballs_dir_dirs:
            shutil.rmtree(targzballs_dir)


def makedirs_downloads():
    for dataset_name in dataset_names:
        download_dir = DOWNLOADS_DIR / f"{dataset_name}"
        download_dir.mkdir()


def download():
    for dataset_name, repo_url_dict in dataset_dict.items():
        print(
            f'downloading data for {dataset_name}'
        )
        local_repo_path = DOWNLOADS_DIR.joinpath(dataset_name)
        prefixes = []

        if 'data_url' in repo_url_dict:
            prefixes.append('data')
        elif 'audio_url' in repo_url_dict and 'annot_url' in repo_url_dict:
            prefixes.append('audio')
            prefixes.append('annot')

        for prefix in prefixes:
            url = repo_url_dict[f'{prefix}_url']
            filename = repo_url_dict[f'{prefix}_filename']
            dst = local_repo_path.joinpath(filename)
            urlcopy(url, dst=str(dst))

            print(
                f'extracting data for {dataset_name}'
            )

            if dst.suffixes[-2:] == ['.tar', '.gz']:
                tar = tarfile.open(str(dst))
                tar.extractall(str(local_repo_path))
            elif dst.suffixes[-1:] == ['.zip']:
                with zipfile.ZipFile(str(dst), 'r') as zip_ref:
                    zip_ref.extractall(str(local_repo_path))
            elif dst.suffixes[-1:] == ['.rar']:
                with rarfile.RarFile(str(dst), 'r') as rar_ref:
                    rar_ref.extractall(str(local_repo_path))


def make_targz(targz_filename, source_dir, open_as="w:gz"):
    with tarfile.open(targz_filename, open_as) as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def targzball():
    for dataset_name in dataset_names:
        func_key = dataset_name.replace('-', '_')
        tarprep_func =tarprep_funcs[func_key]

        data_dir = DOWNLOADS_DIR.joinpath(dataset_name)
        targz_dir = TARGZBALLS_DIR.joinpath(dataset_name)
        tarprep_func(src=data_dir, dst=targz_dir)

        targz = TARGZBALLS_DIR / f'{dataset_name}.tar.gz'
        make_targz(targz_filename=targz, source_dir=targz_dir)


def all():
    makedirs_downloads()
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
    elif command == 'makedirs_downloads':
        makedirs_downloads()
    elif command == 'download':
        download()
    elif command == 'targzball':
        targzball()
    else:
        raise ValueError(
            f'unknown command: {command}'
        )


def get_argparser():
    DESCRIPTION = 'command-line interface for script that generates Pollyglot dataset'
    CHOICES = [
        'clean',
        'all',
        'makedirs_downloads',
        'download',
        'targzball',
    ]

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('command', type=str, metavar='command',
                        choices=CHOICES,
                        help="Command to run, valid options are:\n"
                             f"{CHOICES}\n")
    return parser


def main():
    parser = get_argparser()
    args = parser.parse_args()
    make(args.command)


if __name__ == '__main__':
    main()
