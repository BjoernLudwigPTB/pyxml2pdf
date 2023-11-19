import re
from datetime import date
from typing import Callable, Dict

import pytest
from hypothesis import given, HealthCheck, settings
from hypothesis.strategies import dates, text
from reportlab.platypus.tables import Table  # type: ignore

from pyxml2pdf.core.events import Event
from pyxml2pdf.core.rows import XMLRow


@pytest.fixture
def test_event(test_element) -> Event:
    """Create a test event related to the test_element

    :returns: an event matching the test_element
    """
    return Event(test_element)


@pytest.fixture
def prerequisites() -> Dict[str, str]:
    return {
        "personal": "walk really good",
        "material": "shoes",
        "financial": "100.000",
        "offers": "nothing",
    }


def test_event_init(test_event):
    """Test initialization of :py:mod:`Event` and check for all expected members"""
    assert test_event._criteria
    assert test_event._full_row
    assert isinstance(test_event._init_reduced_row, Callable)
    assert isinstance(test_event.get_full_row, Callable)


def test_event_parent(test_event):
    """Test if parent class of :py:mod:`Event` is :py:mod:`Element`"""
    assert isinstance(test_event, XMLRow)


def test_event_tag(test_element, test_event):
    """Test if tag of initialization element of event is properly processed"""
    assert test_event.tag == test_element.tag


def test_event_attrib(test_element, test_event):
    """Test if attributes of initialization element of event is properly processed"""
    assert test_event.attrib == test_element.attrib


def test_event_call_get_full_row(test_event, subtable_title):
    """get_full_row's return type should be of instance table"""
    assert isinstance(test_event.get_full_row(subtable_title), Table)


def test_event_init_reduced_call(test_event, subtable_title):
    """Reduced row should just be created when init is called on it"""
    with pytest.raises(AttributeError):
        assert test_event._reduced_row
    test_event._init_reduced_row(subtable_title)
    assert test_event._reduced_row


def test_event_get_reduced_row(test_event, subtable_title):
    """Reduced row should be created as just one table row with five columns"""
    test_event._init_reduced_row(subtable_title)
    assert test_event._reduced_row._nrows == 1
    assert test_event._reduced_row._ncols == 2


def test_event_reduced_rows_column_widths(test_event, subtable_title, test_table_style):
    """Reduced row should be created with column widths according to full row

    This test actually makes sense only for the case of data that allows for the
    creation of reduced rows and need to be adapted then to the number of common
    columns.
    """
    test_event._init_reduced_row(subtable_title)
    assert test_event._reduced_row._colWidths[:1] == test_table_style.column_widths[:1]
    assert (
        test_event._reduced_row._colWidths[1]
        == test_event._reduced_row._colWidths[-1]
        == sum(test_table_style.column_widths[1:])
    )


def test_event_reduced_creation(test_event, subtable_title):
    """Reduced row should be created after full row is requested"""
    with pytest.raises(AttributeError):
        assert test_event._reduced_row
    assert test_event.get_full_row(subtable_title)
    assert test_event._reduced_row


def test_event_compare_reduced_row(test_event, subtable_title):
    """Reduced row should contain the same as full up to column 4 but not afterwards"""
    full_row = test_event.get_full_row(subtable_title)
    reduced_row = test_event._reduced_row
    assert str(full_row._cellvalues[0][0]) == str(reduced_row._cellvalues[0][0])
    assert str(full_row._cellvalues[0][:-1]) != str(reduced_row._cellvalues[0][:-1])


def test_event_content_reduced_row(test_event, subtable_title):
    """Reduced row should end with subtable title followed by a period"""
    test_event._init_reduced_row(subtable_title)
    test_string = f"Main entry in subtable '{subtable_title}'."
    assert (
        test_event._reduced_row._cellvalues[0][-1].text[-len(test_string) :]
        == test_string
    )


def test_event_get_row(test_event, subtable_title):
    """Before call to table row no reduced table row should be available"""
    with pytest.raises(AttributeError):
        assert test_event._reduced_row
    assert test_event.get_table_row(subtable_title)
    assert test_event._reduced_row


def test_concatenate_tags_content(test_event):
    test_event._concatenate_tags_content(["test"])


def test_full_call_parse_prerequisites(prerequisites):
    assert (
        Event._parse_prerequisites(**prerequisites)
        == "a) "
        + prerequisites["personal"]
        + "<br/>b) "
        + prerequisites["material"]
        + "<br/>c) "
        + prerequisites["financial"]
        + " € ("
        + prerequisites["offers"]
        + ")"
    )


def test_minimal_call_parse_prerequisites():
    # Check full call.
    assert (
        Event._parse_prerequisites("", "", "", "")
        == "a) keine<br/>b) keine<br/>c) 0,00 €"
    )


@given(text(min_size=1))
def test_call_parse_prerequisites_with_personal(s):
    assert (
        Event._parse_prerequisites(s, "", "", "")
        == "a) " + s + "<br/>b) keine<br/>c) 0,00 €"
    )


@given(text(min_size=1))
def test_call_parse_prerequisites_with_material(s):
    assert (
        Event._parse_prerequisites("", s, "", "")
        == "a) keine<br/>b) " + s + "<br/>c) 0,00 €"
    )


@given(text(min_size=1))
def test_call_parse_prerequisites_with_financial(s):
    assert (
        Event._parse_prerequisites("", "", s, "")
        == "a) keine<br/>b) keine<br/>c) " + s + " €"
    )


@given(text(min_size=1))
def test_call_parse_prerequisites_with_offers(s):
    assert (
        Event._parse_prerequisites("", "", "", s)
        == "a) keine<br/>b) keine<br/>c) 0,00 € (" + s + ")"
    )


@settings(suppress_health_check=(HealthCheck.function_scoped_fixture,))
@given(dates(min_value=date(1000, 1, 1)))
def test_remove_country(test_event, dat):
    assert re.sub(
        "[0-9]{4,}", test_event._remove_century, dat.strftime("%d.%m.%Y")
    ) == dat.strftime("%d.%m.%y")


def test_event_has_property_responsible(test_event):
    assert isinstance(test_event.responsible, str)


def test_event_has_property_identifier(test_event):
    assert isinstance(test_event.responsible, str)
