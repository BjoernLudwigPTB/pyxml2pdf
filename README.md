# pyxml2pdf

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8cd591a0e814ed59f9e6f4a0ac5cf4c)](https://www.codacy.com/manual/blus_projects/pyxml2pdf?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BjoernLudwigPTB/pyxml2pdf&amp;utm_campaign=Badge_Grade)
[![CircleCI](https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf.svg?style=shield)](https://circleci.com/gh/BjoernLudwigPTB/pyxml2pdf)
[![Maintainability](https://api.codeclimate.com/v1/badges/fe9134d2e9449bd42175/maintainability)](https://codeclimate.com/github/BjoernLudwigPTB/pyxml2pdf/maintainability)
[![codecov](https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf/branch/master/graph/badge.svg)](https://codecov.io/gh/BjoernLudwigPTB/pyxml2pdf)
[![Documentation Status](https://readthedocs.org/projects/pyxml2pdf/badge/?version=latest)](https://pyxml2pdf.readthedocs.io/en/latest/?badge=latest)


Convert XML input to PDF table. Since we forked the
[upstream](https://github.com/kuras120/XMLToPDFConverter) this project has generalized
quite a bit on the generation of a multipage PDF file containing a table with
subtables each containing a subset of the xml tags based on the texts of some of
their children tags. Since we work on this project every end of the year, we will
provide an extensive bit of documentation by the end of November 2019.

## Getting started 
As a starting point you could take a look at the execution of
[MainPredefined.py](pyxml2pdf/MainPredefined.py) which will download a publicly available XML
file into the folder *input* and process it as desired to produce the output files
(one file containing all generated pages in landscape and additionally one file per
page rotated into portrait) and place them in the subfolder *output*.

## Documentation

The full developer reference with all public interfaces you can find on [ReadTheDocs
](https://pyxml2pdf.readthedocs.io/). User documentation might still take a while for
us to generate, since it is only us working on the project and using it as far as we
now.
 
 ## Get in touch
 
 In case you have any questions on this project do not hesitate to get in touch with
 [us](https://github.com/BjoernLudwigPTB/pyxml2pdf/graphs/contributors).
