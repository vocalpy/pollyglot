# vocal-annotation-formats
Small example datasets for different formats of annotating vocalizations.

The [Makefile](./Makefile) creates an archive from each subdirectory 
in [data](./data). These are then uploaded to a Figshare dataset repository:  
<https://figshare.com/articles/Vocalization_Annotation_Formats_Dataset/8046920>

The reason for creating this repository is not to use GitHub as a data 
store. The goal is to share code that automates the process of creating a data 
repository on FigShare, and make this source open for collaboration. The 
formats in this repository can be parsed by the 
[Crowsetta](<https://github.com/NickleDave/crowsetta>) package. Development and 
tutorials for `crowsetta` make use of the small, quick-to-download archives of 
each format on Figshare that are generated from the source in this repository.

`crowsetta` provides tools for anyone that wants to write clean code 
when working with these annotion formats (or their own format)
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

### .not.mat
.not.mat files are output by the evsonganaly GUI created by Evren Tumer in the Brainard lab.
The audio file format .cbin is output by the Labview program EvTAF.

Another repository of Bengalese finch song annotated in this format is here:
<https://figshare.com/articles/Bengalese_Finch_song_repository/4805749>

## Project information

### License
Vocal-annotation-formats-dataset (c) by David Nicholson, 2018-2019.

Code is shared under [BSD-3 License](./LICENSE-CODE).

Where applicable, data in the vocal-annotations-formats-dataset is licensed 
under a Creative Commons Attribution-ShareAlike 4.0 International License.
(The figshare repositories are shared under CC-BY-4.0)
Where the authors have not made their intentions clear with a license, 
citations to papers and links to the original source are included.
Please raise an issue on this repository if there are any concerns about this.

You should have received a [copy of the license](./LICENSE-DATA) along with this
work.  If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
