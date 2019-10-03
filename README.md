[![DOI](https://zenodo.org/badge/163442407.svg)](https://zenodo.org/badge/latestdoi/163442407)
[![PyPI version](https://badge.fury.io/py/pollyglot.svg)](https://badge.fury.io/py/pollyglot)
# pollyglot
Small example datasets of annotated vocalizations.

Useful if you have:
- need some example vocalizations that are quick to download
- build a tool that works with different annotation formats
  and you want to test that tool

## usage
There are two components to `pollyglot`:
1. command-line tool that creates the small example datasets from
   larger publicly-available datasets
2. package that fetches the small example datasets, which can be
   a dependency for your library

To use (1), you invoke the command-line tool `pollymake`

Cloning this repository, installing it for development (see below), and then calling
```
$ pollymake all
```
will re-make the dataset within the repository.

`pollymake` creates an archive from each repository. These are then uploaded to a Figshare dataset repository:
<https://figshare.com/articles/pollyglot/9929549>

The goal of this package to share code that automates the process of creating a data
repository on FigShare, and make this source open for collaboration. The 
formats in this repository can be parsed by the 
[Crowsetta](<https://github.com/NickleDave/crowsetta>) package. Development and 
tutorials for `crowsetta` make use of the small, quick-to-download archives of 
each format on Figshare that are generated from the source in this repository.

`crowsetta` provides tools for anyone that wants to write clean code 
when working with these annotation formats (or their own format)
To learn more, please visit <https://github.com/NickleDave/crowsetta>

## formats + references
Below are the formats included and references for the sources.

### Praat textgrid
Textgrids output by the Praat program.

Songs with Praat textgrid format are from the Birdsong Database provided by the
Taylor lab at UCLA:  
<http://taylor0.biology.ucla.edu/birdDBQuery/>  
as presented in this paper: <https://www.sciencedirect.com/science/article/pii/S1574954115000151>
The .xls file containing links to songs from the Taylor lab birdsong database was 
created by Tim Sainburg to train generative networks for animal vocalizations: 
<https://github.com/timsainb/AVGN>; adapted under MIT license.  

### .not.mat
.not.mat files are output by the evsonganaly GUI created by Evren Tumer in the Brainard lab.
The audio file format .cbin is output by the Labview program EvTAF.

Another repository of Bengalese finch song annotated in this format is here:
<https://figshare.com/articles/Bengalese_Finch_song_repository/4805749>

### BirdsongRecognition
A specific .xml format for a repository of labeled Bengalese Finch song.
The repository is here:
<https://figshare.com/articles/BirdsongRecognition/3470165>.
The repository provides data for testing a convolutional neural network to segment 
and label vocalizations, as shared in the repository 
<https://github.com/takuya-koumura/birdsong-recognition>
and discussed in the paper "Automatic recognition of element classes and boundaries in the birdsong 
with variable sequences" by Takuya Koumura and Kazuo Okanoya 
(<http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0159188>).

## Project information

### License
Pollyglot (c) by David Nicholson, 2018-2019.

Code is shared under [BSD-3 License](./LICENSE-CODE).

Where applicable, data in the vocal-annotations-formats-dataset is licensed 
under a Creative Commons Attribution-ShareAlike 4.0 International License.
(The figshare repositories are shared under CC-BY-4.0)
Where the authors have not made their intentions clear with a license, 
citations to papers and links to the original source are included.
Please raise an issue on this repository if there are any concerns about this.

You should have received a [copy of the license](./LICENSE-DATA) along with this
work.  If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
