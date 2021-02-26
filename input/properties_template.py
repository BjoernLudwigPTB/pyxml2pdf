"""This is the set of parameters for interpretation the XML input and formatting"""

from typing import List, NamedTuple, Tuple

#: the page size of the generated Pdf.
pagesize = (90.1, 84.3)


#: The XML tag, which will be represented by one row in the table.
rows_xmltag = "row_tag"

#: The XML tag, which will be used to identify the row for error message printing.
identifier_xmltag = [
    "Name",
    "Info",
]  # type: List[str]

#: The XML tag, which will be represented by one row in the table.
sort_xmltag = "name_tag"

# The table title is displayed as the content of the very first cell in full table
# width.
table_title = "Example Pdf"

Column = NamedTuple("Column", [("label", str), ("tag", List[str]), ("width", float)])
#: The specification for the table columns. The desired column headings are specified
#: as 'label' and the XML tags containing the content to be displayed in the table
#: columns are specified as 'tag'. By default, the content of each tag is transferred
#: to one cell. If several tags are to be merged within one cell, nested lists can be
#: used here. All tags listed here, which finally shall be displayed in the columns of
#: one and the same row, must each belong to one parent tag `rows_xmltag'. The column
#: widths are specified with 'width' in mm.
columns = [
    Column(label="name", tag=["name_tag"], width=30),
    Column(label="info", tag=["info_tag"], width=30),
    Column(label="filter", tag=["filter_tag"], width=30),
]
# The XML tag used to select the respective rows for the subtables.
subtables_xmltag = "filter_tag"

SubtableSetting = NamedTuple(
    "SubtableSetting", [("label", str), ("include", List[List[str]])]
)
# The subtables headings and criteria, i.e. the `subtables_xmltag`'s content,
# which all elements from the XML input should match to be listed in the according
# subtable. There will be one subtable for each set of title and criteria, as long as
# at least one element is found for the subtable. To _match_ the criteria,
# the element's `subtables_xmltag`'s content needs to contain at least one of the
# list elements of each of the nested lists, given here.
subtable_settings = (
    SubtableSetting(label="filter 1", include=[["filter_1"]]),
    SubtableSetting(
        label="filter 1 and filter 2", include=[["filter_1"], ["filter_2"]]
    ),
    SubtableSetting(label="filter 1 or filter 2", include=[["filter_1", "filter_2"]]),
    SubtableSetting(label="filter 2", include=[["filter_2"]]),
    SubtableSetting(
        label="filter 2 and filter 3", include=[["filter_2"], ["filter_3"]]
    ),
    SubtableSetting(label="filter 2 or filter 3", include=[["filter_2", "filter_3"]]),
    SubtableSetting(label="filter 3", include=[["filter_3"]]),
    SubtableSetting(
        label="filter 1 and filter 3", include=[["filter_1"], ["filter_3"]]
    ),
    SubtableSetting(label="filter 1 or filter 3", include=[["filter_1", "filter_3"]]),
)  # type: Tuple[SubtableSetting, ...]

Font = NamedTuple(
    "Font", [("normal", str), ("italic", str), ("bold", str), ("bolditalic", str)]
)
#: Fonts for the table.
font = Font(
    normal="NewsGothicBT-Roman.ttf",
    italic="NewsGothicBT-Italic.ttf",
    bold="NewsGothicBT-Bold.ttf",
    bolditalic="NewsGothicBT-BoldItalic.ttf",
)  # type: Font

FontSize = NamedTuple(
    "FontSize", [("normal", float), ("table_heading", float), ("column_heading", float)]
)
#: Set the font size for the table. 'normal' applies to all text except table and
#: column headings, where 'table_heading' applies to the very first line of the whole
#: table and additionally the first line of all subtables.
fontsize = FontSize(normal=6.5, table_heading=12, column_heading=6.5,)  # type: FontSize
