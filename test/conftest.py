import defusedxml  # type: ignore
import pytest

from pyxml2pdf.core.rows import XMLRow
from pyxml2pdf.styles.table_styles import XMLTableStyle

# Monkeypatch standard library xml vulnerabilities.
defusedxml.defuse_stdlib()
from xml.etree.ElementTree import Element


@pytest.fixture
def test_element() -> Element:
    """Create a test element

    :returns: and element
    """
    test_tag = "test"
    test_attrib1 = "attrib1"
    test_attrib_2 = "attrib2"
    test_attrib = {"1": test_attrib1, "2": test_attrib_2}
    test_element = Element(test_tag, test_attrib)
    return test_element


@pytest.fixture
def subtable_title() -> str:
    """Create a title for a test subtable

    :returns: a test subtable's title
    """
    return "Test subtable title"


@pytest.fixture
def test_table_style() -> XMLTableStyle:
    return XMLTableStyle()


@pytest.fixture
def test_row(test_element) -> XMLRow:
    """Create a test row related to the test_element

    :returns: a row matching the test_element
    """
    return XMLRow(test_element)
