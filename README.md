<p align="center">
  <!-- CircleCI Tests -->
  <a href="https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf"><img alt="CircleCI pipeline status badge" src="https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf.svg?style=shield"></a>
  <!-- ReadTheDocs Documentation -->
  <a href="https://pyxml2pdf.readthedocs.io/en/latest/">
    <img src="https://readthedocs.org/projects/pyxml2pdf/badge/?version=latest" alt="ReadTheDocs badge">
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
this project has generalized quite a bit towards the <b>generation of a multipage PDF
file</b>  containing a table with subtables each containing a subset of an XML files
content arranged in rows and columns. We work on this project mainly every quarter.</p>

## Table of content

- [💫 Quickstart](#quickstart)
- [👓 Example](#example)
- [📖 Documentation](#documentation)
- [💻 Installation](#installation)
- [💨 Coming soon](#coming-soon)
- [👋 Get in touch](#get-in-touch)
- [⚠ Disclaimer](#disclaimer)
- [️© License](#license)

## 💫Quickstart 

As a starting point you could call

```shell
$ python -m main.py input/my_test_download.xml
```

which will download a publicly available XML file into the folder *input* and process
it as desired to produce the output files (one file containing all generated pages in 
landscape and additionally one file per page rotated into portrait) and place them in 
the subfolder *output*.

The intended way of using this software is calling
[_main.py_](pyxml2pdf/main.py) with the following command line parameters

- positional arguments:
  - `<local_file>` The local file path to the XML file. If this file is not present,
    the optional input parameter '--url' needs to be provided with the URL from which
    the file shall be downloaded.

- optional arguments:
  - `-u <URL>, --url <URL>`
    The URL from which the file shall be downloaded. This is only used, if the specified
    local file is not present. Defaults to ['https://www.alpinclub-berlin.de/kv/kursdaten.xml'](https://www.alpinclub-berlin.de/kv/kursdaten.xml)
  - `-p <path to Pdf file>, --pdf <path to Pdf file>`
    The file path to store the created PDF to. Defaults to `'output/kursdaten.pdf'`

## 👓Example

Imagine you have an XML file with similar groups of tags and subtags.

```xml
<main_tag>
    <row_tag>
        <name_tag>Name 1</name_tag>
        <info_tag>Info 1</info_tag>
        <filter_tag>Filter_1-1 Filter_1-2</filter_tag>
    </row_tag>
    <row_tag>
        <name_tag>Name 2</name_tag>
        <info_tag>Info 2</info_tag>
        <filter_tag>Filter_2-1 Filter_2-2 Filter_2-3</filter_tag>
    </row_tag>
    [...]
    <row_tag>
        <name_tag>Name n</name_tag>
        <info_tag>Info n</info_tag>
        <filter_tag>Filter_n-1</filter_tag>
    </row_tag>
</main_tag>
```

Now you want to visualize all `row_tag`s with their subtags `name_tag` and `info_tag`
fed into separate columns. And lastly you want to group those `row_tags` which 
satisfy certain filter criteria, that is their `filter_tag` contains certain
combinations of space-separated texts. Those groups of `row_tag`s are extracted into
several subtables each with a separating heading line and the corresponding column
headings.

![page one of the processed draft.xml](output/draft_seite_01_rotiert.png)

## 📖Documentation

The full developer reference with all public interfaces you can find on [ReadTheDocs
](https://pyxml2pdf.readthedocs.io/). User documentation might still take a while for
us to generate, since it is only us working on the project and using it as far as we
know.

## 💻Installation

The installation of pyxml2pdf is as straightforward as the Python 
ecosystem suggests. Just [create a virtual environment](https://docs.python.org/3/library/venv.html)
and install it via: 

```shell
(venv) $ pip install pyxml2pdf
```

## 💨Coming soon
 
The next big step will be the deployment on [Heroku](https://www.heroku.com).

## 👋Get in touch
 
In case you have any questions on this project do not hesitate to get in touch with
[us](https://github.com/BjoernLudwigPTB/pyxml2pdf/graphs/contributors).

## ⚠Disclaimer

This software is developed in sole responsibility of Björn Ludwig. The software is made
available "as is" free of cost. The author assumes no responsibility whatsoever for its
use by other parties, and makes no guarantees, expressed or implied, about its quality, 
reliability, safety, suitability or any other characteristic. In no event will the 
author be liable for any direct, indirect or consequential damage arising in connection
with the use of this software.
## ©License

pyxml2pdf is distributed under the [GPLv3 license](https://github.com/BjoernLudwigPTB/pyxml2pdf/blob/master/LICENSE).
