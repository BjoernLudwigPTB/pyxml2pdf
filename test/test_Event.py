from xml.etree.ElementTree import Element

import pytest

from Core.events import Event


@pytest.fixture()
def setup_test_element() -> Element:
    """Create the test element

    :returns: the element
    """
    test_tag = "test"
    test_attrib1 = "attrib1"
    test_attrib_2 = "attrib2"
    test_attrib = {"1": test_attrib1, "2": test_attrib_2}
    return Element(test_tag, test_attrib)


def test_event_init(setup_test_element):
    """Test initialization of :py:mod:`Event` and check for all expected attributes"""
    test_event = Event(setup_test_element)
    assert test_event._categories
    assert test_event._full_row


def test_event_parent(setup_test_element):
    """Test if parent class of :py:mod:`Event` is :py:mod:`Element`"""
    test_event = Event(setup_test_element)
    assert isinstance(test_event, Element)


def test_event_tag(setup_test_element):
    """Test if tag of initialization element of event is properly processed"""
    test_event = Event(setup_test_element)
    assert test_event.tag == setup_test_element.tag


def test_event_attrib(setup_test_element):
    """Test if attributes of initialization element of event is properly processed"""
    test_event = Event(setup_test_element)
    assert test_event.attrib == setup_test_element.attrib


def test_event_reduced_creation(setup_test_element):
    """Test if reduced row is created after full row is requested"""
    test_event = Event(setup_test_element)
    assert test_event.attrib == setup_test_element.attrib
