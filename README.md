# pyxml2pdf

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pyxml2pdf)
[![PyPI release number](https://badge.fury.io/py/pyxml2pdf.svg)](https://pypi.org/project/pyxml2pdf/)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8cd591a0e814ed59f9e6f4a0ac5cf4c)](https://www.codacy.com/manual/blus_projects/pyxml2pdf?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BjoernLudwigPTB/pyxml2pdf&amp;utm_campaign=Badge_Grade)
[![CircleCI](https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf.svg?style=shield)](https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf)
[![Maintainability](https://api.codeclimate.com/v1/badges/fe9134d2e9449bd42175/maintainability)](https://codeclimate.com/github/BjoernLudwigPTB/pyxml2pdf/maintainability)
[![codecov](https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf/branch/master/graph/badge.svg)](https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf)
[![Documentation Status](https://readthedocs.org/projects/pyxml2pdf/badge/?version=latest)](https://pyxml2pdf.readthedocs.io/en/latest/?badge=latest)


Convert XML input to PDF table. Since we forked the [upstream](https://github.com/kuras120/XMLToPDFConverter)
this project has generalized a lot towards the generation of a multipage PDF file
containing a table with subtables each containing a subset of the xml tags based on the
texts of some of their children tags.

## Example

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
spread fed into separate columns. And lastly you want to group those `row_tags` which 
satisfy certain filter criteria, that is their `filter_tag` contains certain
combinations of space-separated texts. Those groups of `row_tag`s are extracted into
several subtables each with a separating heading line the corresponding column headings.

## Getting started 

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
  _local_file_ The local file path to the XML file. If this file is not present,
  the optional input parameter '--url' needs to be provided with the URL from which the file shall be downloaded.

- optional arguments:
  -u URL, --url URL
    The URL from which the file shall be downloaded. This is only used, if the specified
    local file is not present. Defaults to ['https://www.alpinclub-berlin.de/kv/kursdaten.xml'](https://www.alpinclub-berlin.de/kv/kursdaten.xml)
  -p <path to Pdf file>, --pdf <path to Pdf file>
    The file path to store the created PDF to. Defaults to `'output/kursdaten.pdf'`

A call thus could look like:

```shell
$ python pyxml2pdf/main.py input/kursdaten.xml
```

## Documentation

The full developer reference with all public interfaces you can find on [ReadTheDocs
](https://pyxml2pdf.readthedocs.io/). User documentation might still take a while for
us to generate, since it is only us working on the project and using it as far as we
know.

## Next steps

The next big step will be the deployment on [Heroku](https://www.heroku.com). 
 
## Get in touch
 
In case you have any questions on this project do not hesitate to get in touch with
[us](https://github.com/BjoernLudwigPTB/pyxml2pdf/graphs/contributors).
