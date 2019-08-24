"""functions that prepare .tar.gz files from downloaded data"""
import shutil


def cbin_notmat(src, dst):
    """creates a tar from the cbin-notmat directory

    Parameters
    ----------
    src : pathlib.Path
        source; a sub-directory in ./results/downloads
    dst : pathlib.Path
        destination; a sub-directory in ./results/targzballs

    Returns
    -------
    None
    """
    SUBDIR = '032212'
    NUM_TO_USE = 20
    exts = ['.cbin', '.not.mat', '.rec']
    exts_files_map = {}
    for ext in exts:
        files_this_ext = sorted(list(
            src.joinpath(SUBDIR).glob(f'*{ext}')
        ))
        files_this_ext = files_this_ext[:NUM_TO_USE]
        exts_files_map[ext] = files_this_ext
    dst.mkdir()
    for _, files in exts_files_map.items():
        for src_file in files:
            dst_file = dst / src_file.name
            shutil.copy(src_file, dst_file)


def wav_koumura(src, dst):
    """creates a tar from the wav-koumura directory

    Parameters
    ----------
    src : pathlib.Path
        source; a sub-directory in ./results/downloads
    dst : pathlib.Path
        destination; a sub-directory in ./results/targzballs

    Returns
    -------
    None
    """
    SUBDIR = 'Bird0/Wave'
    NUM_TO_USE = 20
    exts = ['.wav']
    exts_files_map = {}
    for ext in exts:
        files_this_ext = sorted(list(
            src.joinpath(SUBDIR).glob(f'*{ext}')
        ))
        files_this_ext = files_this_ext[:NUM_TO_USE]
        exts_files_map[ext] = files_this_ext

    # hack
    exts_files_map['.xml'] = [src.joinpath('Bird0/Annotation.xml')]

    dst.mkdir()
    for _, files in exts_files_map.items():
        for src_file in files:
            dst_file = dst / src_file.name
            shutil.copy(src_file, dst_file)


def wav_textgrid(src, dst):
    """creates a tar from the wav-textgrid directory

    Parameters
    ----------
    src : pathlib.Path
        source; a sub-directory in ./results/downloads
    dst : pathlib.Path
        destination; a sub-directory in ./results/targzballs

    Returns
    -------
    None
    """
    NUM_TO_USE = 5
    wav_paths = sorted(list(
        src.joinpath('Wav Files 1').glob('*.WAV')
    ))

    textgrid_dir = src.joinpath('Textgrids')
    exts_files_map = {
        'WAV': [],
        'TextGrid': [],
    }

    num_added = 0
    wav_path_ind = 0
    while num_added < NUM_TO_USE:
        wav_path = wav_paths[wav_path_ind]
        textgrid_name = str(wav_path.name).replace('.WAV', '.TextGrid')
        textgrid_path = textgrid_dir / textgrid_name
        if textgrid_path.exists():
            exts_files_map['WAV'].append(wav_path)
            exts_files_map['TextGrid'].append(textgrid_path)
            num_added += 1
        wav_path_ind += 1
        if wav_path_ind > len(wav_paths) - 1:
            raise ValueError(
                f'was not able to find {NUM_TO_USE} .WAV files '
                f'that had matching .TextGrid files'
            )

    dst.mkdir()
    for _, files in exts_files_map.items():
        for src_file in files:
            dst_file = dst / src_file.name
            shutil.copy(src_file, dst_file)
