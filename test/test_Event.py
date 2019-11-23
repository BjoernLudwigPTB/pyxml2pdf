from xml.etree.ElementTree import Element
from reportlab.platypus.tables import Table

import pytest

from Core.events import Event

from typing import Callable


@pytest.fixture()
def test_element() -> Element:
    """Create the test element

    :returns: the element
    """
    test_tag = "test"
    test_attrib1 = "attrib1"
    test_attrib_2 = "attrib2"
    test_attrib = {"1": test_attrib1, "2": test_attrib_2}
    test_element = Element(test_tag, test_attrib)
    return test_element


@pytest.fixture()
def setup_subtable_title() -> str:
    return "Test subtable title"


def test_event_init(test_element):
    """Test initialization of :py:mod:`Event` and check for all expected members"""
    test_event = Event(test_element)
    assert test_event._categories
    assert test_event._full_row
    assert isinstance(test_event._init_reduced_row, Callable)
    assert isinstance(test_event.get_full_row, Callable)
    assert isinstance(test_event.get_categories, Callable)


def test_event_parent(test_element):
    """Test if parent class of :py:mod:`Event` is :py:mod:`Element`"""
    test_event = Event(test_element)
    assert isinstance(test_event, Element)


def test_event_tag(test_element):
    """Test if tag of initialization element of event is properly processed"""
    test_event = Event(test_element)
    assert test_event.tag == test_element.tag


def test_event_attrib(test_element):
    """Test if attributes of initialization element of event is properly processed"""
    test_event = Event(test_element)
    assert test_event.attrib == test_element.attrib


def test_event_call_get_full_row(test_element):
    """Test if get_full_row's return type matches expectations"""
    test_event = Event(test_element)
    assert isinstance(test_event.get_full_row(), Table)


def test_event_init_reduced_call(test_element, setup_subtable_title):
    """Test if reduced row is created after full row is requested"""
    test_event = Event(test_element)
    test_event._init_reduced_row(setup_subtable_title)
    assert test_event._reduced_row


def test_event_reduced_creation(test_element):
    """Test if reduced row is created after full row is requested"""
    test_event = Event(test_element)

    # assert test_event._reduced_row
