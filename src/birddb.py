"""
for downloading files with Praat textgrid annotations from bird database

to convert links in BIRD_DB.xls to urls, I did the following:
- save as .fods format from LibreOffice calc
- open with Notepad++ and use regular expressions with Find-Replace (Ctrl+H):
- Find: (http.*)(" xlink:type="simple">)([^<]*)(</text:a>)
- Replace: $1$2$1$4
- (tried with Gedit first but the replace did not work properly)
"""
import os
import csv
import urllib.request

HERE = os.path.dirname(__file__)
DATA_PATH = os.path.join(HERE, '..', 'data')
BIRD_DB_CSV = os.path.join(DATA_PATH, 'BIRD_DB.csv')
NUM_FILES = 20


def main():
    with open(BIRD_DB_CSV, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row, _ in zip(reader, range(NUM_FILES)):
            for url in (row['Audio_file'], row['Textgrid_file']):
                fname = os.path.join(
                    DATA_PATH, os.path.basename(url)
                )
                urllib.request.urlretrieve(url, fname)

if __name__ == '__main__':
    main()
