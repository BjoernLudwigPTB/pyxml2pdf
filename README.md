<p align="center">
  <!-- CircleCI Tests -->
  <a href="https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf"><img alt="CircleCI pipeline status badge" src="https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf.svg?style=shield"></a>
  <!-- ReadTheDocs Documentation -->
  <a href="https://pyxml2pdf.readthedocs.io/en/latest/">
    <img src="https://readthedocs.org/projects/pyxml2pdf/badge/?version=latest" alt="ReadTheDocs badge">
  </a>
  <!-- CodeClimate Maintainability -->
  <a href="https://codeclimate.com/github/BjoernLudwigPTB/pyxml2pdf/maintainability">
    <img src="https://api.codeclimate.com/v1/badges/fe9134d2e9449bd42175/maintainability" alt="CodeClimate badge">
  </a>
  <!-- Codacy Code Quality -->
  <a href="https://www.codacy.com/manual/blus_projects/pyxml2pdf?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BjoernLudwigPTB/pyxml2pdf&amp;utm_campaign=Badge_Grade">
    <img src="https://api.codacy.com/project/badge/Grade/d8cd591a0e814ed59f9e6f4a0ac5cf4c" alt="Codacy badge">
  </a>
  <!-- CodeCov(erage) -->
  <a href="https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf">
    <img src="https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf/branch/master/graph/badge.svg"/>
  </a>
  <!-- PyPI Version -->
  <a href="https://pypi.org/project/pyxml2pdf">
    <img src="https://img.shields.io/pypi/v/pyxml2pdf.svg?label=release&color=blue&style=flat-square" alt="pypi">
  </a>
  <!-- PyPI Python Version -->
  <a href="https://pypi.org/project/pyxml2pdf">
    <img src="https://img.shields.io/pypi/pyversions/pyxml2pdf" alt="Python Version">
  </a>
  <!-- PyPI License -->
  <a href="https://www.gnu.org/licenses/lgpl-3.0.en.html">
    <img alt="PyPI - license badge" src="https://img.shields.io/pypi/l/pyxml2pdf?color=bright">
  </a>
</p>

<h1 align="center">Convert your XML into a Pdf table</h1>

<p align="justify">
Since we forked the <a href="https://github.com/kuras120/XMLToPDFConverter">upstream</a>
this project has generalized quite a bit towards the generation of a multipage PDF file 
containing a table with subtables each containing a subset of the xml tags based on the 
texts of some of their children tags. We work on this project mainly every end of a
quarter.
</p>

## Table of content

- [💫 Quickstart](#quickstart)
- [📖 Documentation](#documentation)
- [💻 Installation](#installation)
- [💨 Coming soon](#coming-soon)
- [👋 Get in touch](#get-in-touch)
- [⚠ Disclaimer](#disclaimer)
- [️© License](#license)

## 💫 Quickstart 

As a starting point you could take a look at the execution of
[main.py](pyxml2pdf/main.py) which will download a publicly
available XML file into the folder *input* and process it as desired to produce the
output files (one file containing all generated pages in landscape and additionally
one file per page rotated into portrait) and place them in the subfolder *output*.

The intended way of using this software is calling
[_main.py_](pyxml2pdf/main.py) with the following command line parameters

1. The URL to download XML file from if it is not present at the specified location.
1. The file path to store (or open if it exists) the XML file locally.
1. The file path to store the created PDF to.
   
A call thus could look like:

```shell
$ python pyxml2pdf/main.py https://www.alpinclub-berlin.de/kv/kursdaten.xml input/2021_02_kursdaten.xml output/2021_02_kursdaten.pdf
```

## 📖 Documentation

The full developer reference with all public interfaces you can find on [ReadTheDocs
](https://pyxml2pdf.readthedocs.io/). User documentation might still take a while for
us to generate, since it is only us working on the project and using it as far as we
know.

## 💻 Installation

The installation of pyxml2pdf is as straightforward as the Python 
ecosystem suggests. Just [create a virtual environment](https://docs.python.org/3/library/venv.html)
and install it via: 

```shell
(venv) $ pip install pyxml2pdf
```

## 💨 Coming soon
 
The next big step will be the deployment on [Heroku](https://www.heroku.com).


## 👋 Get in touch
 
In case you have any questions on this project do not hesitate to get in touch with
[us](https://github.com/BjoernLudwigPTB/pyxml2pdf/graphs/contributors).

## ⚠ Disclaimer

This software is developed in sole responsibility of Björn Ludwig. The software is made
available "as is" free of cost. The author assumes no responsibility whatsoever for its
use by other parties, and makes no guarantees, expressed or implied, about its quality, 
reliability, safety, suitability or any other characteristic. In no event will the 
author be liable for any direct, indirect or consequential damage arising in connection
with the use of this software.

## © License

pyxml2pdf is distributed under the [GPLv3 license](https://github.com/BjoernLudwigPTB/pyxml2pdf/blob/master/LICENSE).