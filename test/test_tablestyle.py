import pytest
from reportlab.lib.colors import Color  # type: ignore
from reportlab.lib.styles import StyleSheet1  # type: ignore
from reportlab.platypus import TableStyle  # type: ignore

from pyxml2pdf.styles.table_styles import XMLTableStyle


@pytest.fixture(scope="module")
def tablestyle():
    return XMLTableStyle()


def test_tablestyle_custom_styles(tablestyle):
    # Check types and shape of `custom_styles`.
    assert isinstance(tablestyle.custom_styles, dict)
    assert "heading" in tablestyle.custom_styles
    assert "normal" in tablestyle.custom_styles
    assert "sub_heading" in tablestyle.custom_styles
    assert "stylesheet" in tablestyle.custom_styles
    for key, style in (
        (key, style)
        for key, style in tablestyle.custom_styles.items()
        if not key == "stylesheet"
    ):
        assert isinstance(key, str)
        assert isinstance(style, TableStyle)
        for style_element in style.getCommands():
            assert isinstance(style_element, tuple)
            for style_element_atom in style_element:
                assert (
                    isinstance(style_element_atom, tuple)
                    or isinstance(style_element_atom, str)
                    or isinstance(style_element_atom, int)
                    or isinstance(style_element_atom, float)
                    or isinstance(style_element_atom, Color)
                )
                if isinstance(style_element_atom, tuple):
                    assert len(style_element_atom) == 2
    assert isinstance(tablestyle._custom_styles["stylesheet"], StyleSheet1)


def test_tablestyle_column_widths(tablestyle):
    # Check types and shape of `column_widths`.
    assert tablestyle.column_widths
    assert isinstance(tablestyle.column_widths, list)
    for width in tablestyle.column_widths:
        assert float(width)


def test_tablestyle_table_width(tablestyle):
    """Check type of `table_width`."""
    assert isinstance(tablestyle.table_width, float)
    assert tablestyle.table_width


def test_tablestyle__init_font_family_call(tablestyle):
    """Check if initialisation of font family runs without error and returns nothing."""
    assert tablestyle._init_font_family() is None
