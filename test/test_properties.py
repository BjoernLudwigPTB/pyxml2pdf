import pathlib

from input.properties_template import (  # type: ignore
    Column,
    columns,
    font,
    Font,
    fontsize,
    FontSize,
    pagesize,
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
    assert sum(column.width for column in columns) < pagesize[0]


def test_subtables_xmltag():
    # Check type of `subtables_xmltag`.
    assert isinstance(subtables_xmltag, str)


def test_subtables():
    # Check types and shape of `subtables`.
    assert isinstance(subtable_settings, tuple)
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
    assert isinstance(font, Font)
    assert len(font) == 4
    assert "normal" in font._fields
    assert "italic" in font._fields
    assert "bold" in font._fields
    assert "bolditalic" in font._fields

    # Initialize path to fonts, to check for existence.
    path_to_fonts = pathlib.PurePath(__file__).parent.joinpath("fonts")

    for name in font:
        assert isinstance(name, str)
        pathlib.Path(path_to_fonts.joinpath(name)).exists()


def test_fontsize():
    # Check types and shape of `fontsize`.
    assert isinstance(fontsize, FontSize)
    assert len(fontsize) == 3
    assert "normal" in fontsize._fields
    assert "table_heading" in fontsize._fields
    assert "column_heading" in fontsize._fields
    for size in fontsize:
        assert float(size)
