from reportlab.lib.colors import Color  # type: ignore
from reportlab.lib.styles import StyleSheet1  # type: ignore
from reportlab.platypus import TableStyle  # type: ignore


def test_tablestyle_custom_styles(test_table_style):
    # Check types and shape of `custom_styles`.
    assert isinstance(test_table_style.custom_styles, dict)
    assert "heading" in test_table_style.custom_styles
    assert "normal" in test_table_style.custom_styles
    assert "sub_heading" in test_table_style.custom_styles
    assert "stylesheet" in test_table_style.custom_styles
    for key, style in (
        (key, style)
        for key, style in test_table_style.custom_styles.items()
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
    assert isinstance(test_table_style._custom_styles["stylesheet"], StyleSheet1)


def test_tablestyle_column_widths(test_table_style):
    # Check types and shape of `column_widths`.
    assert test_table_style.column_widths
    assert isinstance(test_table_style.column_widths, list)
    for width in test_table_style.column_widths:
        assert float(width)


def test_tablestyle_table_width(test_table_style):
    """Check type of `table_width`."""
    assert isinstance(test_table_style.table_width, float)
    assert test_table_style.table_width


def test_tablestyle__init_font_family_call(test_table_style):
    """Check if initialisation of font family runs without error and returns nothing."""
    assert test_table_style._init_font_family() is None
