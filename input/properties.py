"""The applied set of parameters for interpreting the XML input and output formatting

To change these setting just take any of the provided variables and overwrite it with
your desired value in *input/custom_properties.py*. I.e. to change the :attr:`pagesize`
to something a bit smaller than ISO A5 put the following into
*input/custom_properties.py*:

.. code-block:: python
   :linenos:

   pagesize = (178, 134)
"""
from typing import List, Tuple

from pyxml2pdf.core.types import Column, Font, FontSize, PageSize, SubtableSetting
from . import custom_properties


def _inform_about_fallback_setting(
    fallback_setting_name: str, fallback_setting_value: object
):
    """Inform user about the absence of a custom value for one of the settings"""
    print(
        f"No custom setting found for '{fallback_setting_name}', falling back to "
        f"{fallback_setting_value}."
    )


pagesize: PageSize
"""The page size of the output Pdf in mm"""

try:
    pagesize = custom_properties.pagesize
except AttributeError:
    pagesize = (90.1, 84.3)
    _inform_about_fallback_setting("pagesize", pagesize)

rows_xmltag: str
"""The XML tag, which will be represented by one row in the table"""
try:
    rows_xmltag = custom_properties.rows_xmltag
except AttributeError:
    rows_xmltag = "row_tag"
    _inform_about_fallback_setting("rows_xmltag", rows_xmltag)

identifier_xmltag: List[str]
"""The XML tag, which will be used to identify the row for error message printing

This is used in case an instance of :attr:`rows_xmltag` in the input XML file does 
match any filter criteria and thus would not be included in the output. This results in
an error message telling which element is not printed where :attr:`identifier_xmltag` is
used to inform about which element is affected. The error message starts with 
something close to::

    XML row identified by <IDENTIFIER_XMLTAG's CONTENT> would not be printed, 
    because it does not contain a valid combination of criteria.
"""
try:
    identifier_xmltag = custom_properties.identifier_xmltag
except AttributeError:
    identifier_xmltag = [
        "name_tag",
        "info_tag",
        "filter_tag",
    ]
    _inform_about_fallback_setting("identifier_xmltag", identifier_xmltag)

sort_xmltag: str
"""The XML tag, which will be used to sort the tables' rows

If possible the tags' contents will be sorted as dates otherwise they will be sorted
alphanumerically, each in ascending order.
"""
try:
    sort_xmltag = custom_properties.sort_xmltag
except AttributeError:
    sort_xmltag = "name_tag"
    _inform_about_fallback_setting("sort_xmltag", sort_xmltag)

columns: List[Column]
"""This is of what and how to include into output's columns

The desired column headings in the output are supposed to be specified as 'label' and 
the XML tags containing the content to be displayed in the corresponding rows of the
output's column are supposed to be specified as 'tag'. By default,
the content of each tag is transferred to one cell. If several tags are to be merged
within one cell, nested lists can be used here. All tags listed here, which finally
shall be displayed in the columns of one and the same row, must each belong to one
parent tag :attr:`rows_xmltag`. The column widths are specified with 'width' in mm.
"""
try:
    columns = custom_properties.columns
except AttributeError:
    columns = [
        Column(label="name", tag=["name_tag"], width=30),
        Column(label="info", tag=["info_tag"], width=30),
        Column(label="filter", tag=["filter_tag"], width=30),
    ]
    _inform_about_fallback_setting("columns", columns)

filter_xmltag: str
"""The XML tag used to check for filter criteria in the respective rows"""
try:
    filter_xmltag = custom_properties.filter_xmltag
except AttributeError:
    filter_xmltag = "filter_tag"
    _inform_about_fallback_setting("filter_xmltag", filter_xmltag)

subtable_settings: Tuple[SubtableSetting, ...]
"""The subtables' headings and filter criteria to choose the XML's content to display

There will be one subtable for each set of a label and include 
filter-criteria, as long as at least one element is found for the subtable. To 
*match* the criteria, the element's :attr:`filter_xmltag`'s content needs to contain at 
least one of the list elements of each of the nested lists, given here. The
:attr:`filter_xmltag`'s content will be compared against the given include filters, 
where for comma-separated elements of one list a boolean OR is used and a
boolean AND for the separate lists.
"""
try:
    subtable_settings = custom_properties.subtable_settings
except AttributeError:
    subtable_settings = (
        SubtableSetting(label="filter 1", include=[["filter_1"]]),
        SubtableSetting(
            label="filter 1 and filter 2", include=[["filter_1"], ["filter_2"]]
        ),
        SubtableSetting(
            label="filter 1 or filter 2", include=[["filter_1", "filter_2"]]
        ),
        SubtableSetting(label="filter 2", include=[["filter_2"]]),
        SubtableSetting(
            label="filter 2 and filter 3", include=[["filter_2"], ["filter_3"]]
        ),
        SubtableSetting(
            label="filter 2 or filter 3", include=[["filter_2", "filter_3"]]
        ),
        SubtableSetting(label="filter 3", include=[["filter_3"]]),
        SubtableSetting(
            label="filter 1 and filter 3", include=[["filter_1"], ["filter_3"]]
        ),
        SubtableSetting(
            label="filter 1 or filter 3", include=[["filter_1", "filter_3"]]
        ),
    )
    _inform_about_fallback_setting("subtable_settings", subtable_settings)

font: Font
"""Fonts for the output

Files with the respective file names are expected to be found inside the subfolder
*pyxml2pdf/styles/fonts/*.
"""
try:
    font = custom_properties.font
except AttributeError:
    font = Font(
        normal="LiberationSans-Regular.ttf",
        italic="LiberationSans-Italic.ttf",
        bold="LiberationSans-Bold.ttf",
        bolditalic="LiberationSans-BoldItalic.ttf",
    )
    _inform_about_fallback_setting("font", font)

fontsize: FontSize
"""Set the font size for the table.

This is the font sizes used throughout the output table, where *normal* applies to all
text except table and column headings.
"""
try:
    fontsize = custom_properties.fontsize
except AttributeError:
    fontsize = FontSize(
        normal=6.5,
        table_heading=12,
        column_heading=6.5,
    )
    _inform_about_fallback_setting("fontsize", fontsize)
