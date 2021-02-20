import pathlib

from input.properties import (  # type: ignore
    Column,
    columns,
    font,
    fontsize,
    rows_xmltag,
    subtable_settings,
    subtables_xmltag,
    SubtableSetting,
    table_title,
)


def test_rows_xmltag():
    # Check type of `rows_xmltag`.
    assert isinstance(rows_xmltag, str)


def test_table_title():
    # Check type of `table_title`.
    assert isinstance(table_title, str)


def test_columns():
    # Check types and shape `columns`.
    assert isinstance(columns, list)
    for column in columns:
        assert isinstance(column, Column)
        assert len(column) == 3
        assert isinstance(column.label, str)
        assert isinstance(column.tag, list)
        for tag in column.tag:
            assert isinstance(tag, str)
        assert float(column.width)


def test_column_widths():
    # Check if column widths sum up to 177.8mm.
    assert sum(column.width for column in columns) == 177.8


def test_subtables_xmltag():
    # Check type of `subtables_xmltag`.
    assert isinstance(subtables_xmltag, str)


def test_subtables():
    # Check types and shape of `subtables`.
    assert isinstance(subtable_settings, list)
    for subtable in subtable_settings:
        assert isinstance(subtable, SubtableSetting)
        assert len(subtable) == 2
        assert isinstance(subtable.label, str)
        assert isinstance(subtable.include, list)
        for criteria_list in subtable.include:
            assert isinstance(criteria_list, list)
            for criteria in criteria_list:
                assert isinstance(criteria, str)


def test_font():
    # Check types and shape of `font` and if specified files exist.
    assert isinstance(font, dict)
    assert len(font) == 4
    assert "normal" in font
    assert "italic" in font
    assert "bold" in font
    assert "bolditalic" in font

    # Initialize path to fonts, to check for existence.
    path_to_fonts = pathlib.PurePath(__file__).parent.joinpath("fonts")

    for key in font:
        assert isinstance(key, str)
        assert isinstance(font[key], str)
        pathlib.Path(path_to_fonts.joinpath(font[key])).exists()


def test_fontsize():
    # Check types and shape of `fontsize`.
    assert isinstance(fontsize, dict)
    assert len(fontsize) == 3
    assert "normal" in fontsize
    assert "table_heading" in fontsize
    assert "column_heading" in fontsize
    for key in fontsize:
        assert isinstance(key, str)
        assert float(fontsize[key])
