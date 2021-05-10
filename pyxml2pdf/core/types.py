"""These are custom type variables used for specifying properties"""
from typing import List, NamedTuple, Tuple

SubtableSetting = NamedTuple(
    "SubtableSetting", [("label", str), ("include", List[List[str]])]
)
"""The subtables headings and :attr:`filter_xmltag`'s content

All tags from the XML file which are supposed to be listed in the respective subtable
should match at least one of each of the sublists include-filters. There will be one
subtable for each set of label and include-filters, as long as at least one element
is found for the subtable.
"""

TagList = List[str]
"""List of XML tags"""

Column = NamedTuple("Column", [("label", str), ("tag", TagList), ("width", float)])
"""The custom type of our column specification

This is a `type variable <https://docs.python.org/3/library/typing.html#typing
.TypeVar>`_ to specify in which way we expect the column settings to be provided.
"""

Font = NamedTuple(
    "Font", [("normal", str), ("italic", str), ("bold", str), ("bolditalic", str)]
)
"""The custom type of our font specification

A set of font filenames in ttf format to be used for all of the output's text
"""

FontSize = NamedTuple(
    "FontSize", [("normal", float), ("table_heading", float), ("column_heading", float)]
)
"""The custom type of our fontsize specification"""

PageSize = Tuple[float, float]
"""The custom type for the page size specification in mm"""
