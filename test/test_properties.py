import pathlib

from pyxml2pdf.core.types import Column, Font, FontSize  # type: ignore
from pyxml2pdf.input.properties import (
    COLUMNS,
    FILTER_XMLTAG,
    FONT,
    FONTSIZE,
    IDENTIFIER_XMLTAG,
    PAGESIZE,
    ROWS_XMLTAG,
    SORT_XMLTAG,
    SUBTABLE_SETTINGS,
    SubtableSetting,  # type: ignore
)


def test_rows_xmltag():
    # Check type of `ROWS_XMLTAG`.
    assert isinstance(ROWS_XMLTAG, str)


def test_identifier_xmltag():
    # Check type of `IDENTIFIER_XMLTAG`.
    assert isinstance(IDENTIFIER_XMLTAG, list)
    for tag in IDENTIFIER_XMLTAG:
        assert isinstance(tag, str)


def test_columns():
    # Check types and shape `COLUMNS`.
    assert isinstance(COLUMNS, list)
    for column in COLUMNS:
        assert isinstance(column, Column)
        assert len(column) == 3
        assert isinstance(column.label, str)
        assert isinstance(column.tag, list)
        for tag in column.tag:
            assert isinstance(tag, str)
        assert float(column.width)


def test_pagesize():
    # Check if pagesize is of correct type and size.
    assert isinstance(PAGESIZE, tuple)
    assert len(PAGESIZE) == 2
    for size in PAGESIZE:
        assert isinstance(size, float)


def test_column_widths():
    # Check if column widths match pagesize.
    assert sum(column.width for column in COLUMNS) <= PAGESIZE[0]


def test_filter_xmltag():
    # Check type of `FILTER_XMLTAG`.
    assert isinstance(FILTER_XMLTAG, str)


def test_sort_xmltag():
    # Check type of `SORT_XMLTAG`.
    assert isinstance(SORT_XMLTAG, str)


def test_subtables():
    # Check types and shape of `subtables`.
    assert isinstance(SUBTABLE_SETTINGS, tuple)
    for subtable in SUBTABLE_SETTINGS:
        assert isinstance(subtable, SubtableSetting)
        assert len(subtable) == 2
        assert isinstance(subtable.label, str)
        assert isinstance(subtable.include, list)
        for criteria_list in subtable.include:
            assert isinstance(criteria_list, list)
            for criteria in criteria_list:
                assert isinstance(criteria, str)


def test_font():
    # Check types and shape of `FONT` and if specified files exist.
    assert isinstance(FONT, Font)
    assert len(FONT) == 4
    assert "normal" in FONT._fields
    assert "italic" in FONT._fields
    assert "bold" in FONT._fields
    assert "bolditalic" in FONT._fields

    # Initialize path to fonts, to check for existence.
    path_to_fonts = pathlib.PurePath(__file__).parent.joinpath("fonts")

    for name in FONT:
        assert isinstance(name, str)
        pathlib.Path(path_to_fonts.joinpath(name)).exists()


def test_fontsize():
    # Check types and shape of `FONTSIZE`.
    assert isinstance(FONTSIZE, FontSize)
    assert len(FONTSIZE) == 3
    assert "normal" in FONTSIZE._fields
    assert "table_heading" in FONTSIZE._fields
    assert "column_heading" in FONTSIZE._fields
    for size in FONTSIZE:
        assert float(size)
