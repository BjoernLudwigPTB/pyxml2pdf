import pytest
from reportlab.lib.colors import Color  # type: ignore
from reportlab.lib.styles import StyleSheet1  # type: ignore

from pyxml2pdf.styles.table_styles import TableStyle


@pytest.fixture(scope="module")
def tablestyle():
    return TableStyle()


def test_tablestyle_custom_styles(tablestyle):
    # Check types and shape of `_custom_styles`.
    assert isinstance(tablestyle._custom_styles, dict)
    assert "heading" in tablestyle._custom_styles
    assert "normal" in tablestyle._custom_styles
    assert "sub_heading" in tablestyle._custom_styles
    assert "stylesheet" in tablestyle._custom_styles
    for style in (
        style
        for style in tablestyle._custom_styles.items()
        if not style[0] == "stylesheet"
    ):
        assert isinstance(style[0], str)
        assert isinstance(style[1], list)
        for style_element in style[1]:
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
    # Before table_width was initially requested via the appropriate property method,
    # it will not be initialized and thus an AttributeError is thrown. Afterwards
    # the direct access should work as well.
    with pytest.raises(AttributeError):
        assert tablestyle._table_width
    # Check type of `table_width`.
    assert isinstance(tablestyle.table_width, float)
    assert tablestyle._table_width


def test_tablestyle__init_font_family_call(tablestyle):
    assert tablestyle._init_font_family() is None
