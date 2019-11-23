# XMLtoPDFConverter
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/d8cd591a0e814ed59f9e6f4a0ac5cf4c)](https://www.codacy.com/app/PTB_PSt1/XMLToPDFConverter?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=BjoernLudwigPTB/XMLToPDFConverter&amp;utm_campaign=Badge_Grade)
[![CircleCI](https://circleci.com/gh/BjoernLudwigPTB/XMLToPDFConverter.svg?style=shield)](https://circleci.com/gh/BjoernLudwigPTB/XMLToPDFConverter)
[![Maintainability](https://api.codeclimate.com/v1/badges/462d32995c5cc87af346/maintainability)](https://codeclimate.com/github/BjoernLudwigPTB/XMLToPDFConverter/maintainability)
[![codecov](https://codecov.io/gh/BjoernLudwigPTB/XMLToPDFConverter/branch/master/graph/badge.svg)](https://codecov.io/gh/BjoernLudwigPTB/XMLToPDFConverter)

Convert XML input to PDF table. Since we forked the
[upstream](https://github.com/kuras120/XMLToPDFConverter) this project has generalized
quite a bit on the generation of a multipage PDF file containing a table with
subtables each containing a subset of the xml tags based on the texts of some of
their children tags. Since we work on this project every end of the year, we will
provide an extensive bit of documentation by the end of November 2019.

## Getting started 
As a starting point you could take a look at the execution of
[MainPredefined.py](MainPredefined.py) which will download a publicly available XML
file into the folder *input* and process it as desired to produce the output files
(one file containing all generated pages in landscape and additionally one file per
page rotated into portrait) and place them in the subfolder *output*.
 
 ## Get in touch
 In case you have any questions on this project do not hesitate to get in touch with
 [us](https://github.com/BjoernLudwigPTB/XMLToPDFConverter/graphs/contributors).
