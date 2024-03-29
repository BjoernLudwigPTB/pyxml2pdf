import pytest
from hypothesis import given, HealthCheck, settings, strategies as hst
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  # type: ignore

from pyxml2pdf.core.rows import XMLCell
from pyxml2pdf.core.types import SubtableSetting  # type: ignore
from pyxml2pdf.input.properties import SUBTABLE_SETTINGS  # type: ignore


@pytest.fixture
def test_table_settings() -> SubtableSetting:
    return SUBTABLE_SETTINGS[0]


@pytest.fixture
def test_xmlcell_class(test_table_style):
    my_cell_class = XMLCell
    my_cell_class.style = (  # type: ignore[method-assign]
        test_table_style.custom_styles["stylesheet"]["Normal"]
    )
    return my_cell_class


@settings(suppress_health_check=(HealthCheck.function_scoped_fixture,))
@given(text=hst.text(alphabet=hst.characters(min_codepoint=101, max_codepoint=126)))
def test_xmlcell(test_xmlcell_class, text):
    my_cell = test_xmlcell_class(text)
    assert isinstance(my_cell, XMLCell)
    assert isinstance(my_cell.style, ParagraphStyle)
    assert my_cell.text == text


def test_xmlcell_get_style(test_xmlcell_class):
    """Test, if style getter works"""
    assert isinstance(test_xmlcell_class("test content").style, ParagraphStyle)


def test_xmlcell_set_style(test_xmlcell_class, test_table_style):
    """Test, if style getter works"""
    test_xmlcell_instance = test_xmlcell_class("test content")
    old_style = test_xmlcell_instance.style
    test_xmlcell_instance.style = getSampleStyleSheet()  # type: ignore[method-assign]
    assert old_style != test_xmlcell_instance.style
