# The XML tag, which will be represented by one row in the table.
rows_xmltag = "row_tag"

#: The XML tag, which will be used to identify the row for error message printing.
identifier_xmltag = [
    "TerminDatumVon1",
    "TerminDatumBis1",
    "TerminDatumVon2",
    "TerminDatumBis2",
    "TerminDatumVon3",
    "TerminDatumBis3",
]  # type: List[str]

# The table title is displayed as the content of the very first cell in full table
# width.
table_title = "Example Pdf"

# The specification for the table columns. The desired column headings are specified
# as 'label' and the XML tags containing the content to be displayed in the table
# columns are specified as 'tag'. By default, the content of each tag is transferred
# to one cell. If several tags are to be merged within one cell, nested lists can be
# used here. All tags listed here, which finally shall be displayed in the columns of
# one and the same row, must each belong to one parent tag `rows_xmltag'. The column
# widths are specified with 'width' in mm.
columns = [
    {"label": "Name", "tag": ["name_tag"], "width": 30},
    {"label": "Info", "tag": ["info_tag"], "width": 30},
    {"label": "Filter", "tag": ["filter_tag"], "width": 120},
]
# The XML tag used to select the respective rows for the subtables.
subtables_xmltag = "filter_tag"

# The subtables headings and criteria, i.e. the `subtables_xmltag`'s content,
# which all elements from the XML input should match to be listed in the according
# subtable. There will be one subtable for each set of title and criteria, as long as
# at least one element is found for the subtable. To _match_ the criteria,
# the element's `subtables_xmltag`'s content needs to contain at least one of the
# list elements of each of the nested lists, given here.
subtables = [
    {"label": "Filter 1", "content": [["Filter_1"]]},
    {"label": "Filter 1 und Filter 2", "content": [["Filter_1"], ["Filter_2"]]},
    {"label": "Filter 1 oder Filter 2", "content": [["Filter_1", "Filter_2"]]},
    {"label": "Filter 2", "content": [["Filter_2"]]},
    {"label": "Filter 2 und Filter 3", "content": [["Filter_2"], ["Filter_3"]]},
    {"label": "Filter 2 oder Filter 3", "content": [["Filter_2", "Filter_3"]]},
    {"label": "Filter 3", "content": [["Filter_3"]]},
    {"label": "Filter 1 und Filter 3", "content": [["Filter_1"], ["Filter_3"]]},
    {"label": "Filter 1 oder Filter 3", "content": [["Filter_1", "Filter_3"]]},
]

# Set font for the table.
font = {
    "normal": "NewsGothicBT-Roman.ttf",
    "italic": "NewsGothicBT-Italic.ttf",
    "bold": "NewsGothicBT-Bold.ttf",
    "bolditalic": "NewsGothicBT-BoldItalic.ttf",
}

# Set the font size for the table. 'normal' applies to all text except table and
# column headings, where 'table_heading' applies to the very first line of the whole
# table and additionally the first line of all subtables.
fontsize = {"normal": 6.5, "table_heading": 12, "column_heading": 6.5}
