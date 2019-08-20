"""

"""
from math import ceil

import requests
from tqdm import tqdm

CHUNK_SIZE = 1024 * 10


def urlcopy(url, dst, stream=True, chunk_size=CHUNK_SIZE):
    """copy a file from a url to a local destination

    Parameters
    ----------
    url : str
        url that points to a data file, e.g. a .tar.gz or .zip
    dst : str
        destination, path to where file should be downloaded
    stream : bool
        if True, open url in streaming mode. Default is True.
    chunk_size : int
        number of bytes to read into memory from stream at once.
        Default is 10240.

    Returns
    -------

    """
    response = requests.get(url, stream=stream)
    content_length = int(response.headers['content-length'])

    num_chunks = int(
        ceil(content_length / chunk_size)
    )

    iter_content = response.iter_content(CHUNK_SIZE)
    if response.status_code == 200:
        with open(dst, 'wb') as fp:
            for chunk in tqdm(iter_content, total=num_chunks):
                fp.write(chunk)
    else:
        raise ValueError(
            f'was unable to request content at {url},\n'
            f'got status code {response.status_code} instead of '
            'status code 200 (HTTP OK response)'
        )