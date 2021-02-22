from typing import Callable

import defusedxml  # type: ignore
from reportlab.platypus.tables import Table  # type: ignore

# Monkeypatch standard library xml vulnerabilities.
defusedxml.defuse_stdlib()
from xml.etree.ElementTree import Element


def test_row_init(test_row):
    """Test initialization of :py:mod:`Event` and check for all expected members"""
    assert test_row._criteria
    assert test_row._full_row
    assert isinstance(test_row.get_full_row, Callable)


def test_row_parent(test_row):
    """Test if parent class of :py:mod:`XMLRow` is :py:mod:`Element`"""
    assert isinstance(test_row, Element)


def test_row_tag(test_element, test_row):
    """Test if tag of initialization element of row is properly processed"""
    assert test_row.tag == test_element.tag


def test_row_attrib(test_element, test_row):
    """Test if attributes of initialization element of row is properly processed"""
    assert test_row.attrib == test_element.attrib


def test_row_call_get_full_row(test_row, subtable_title):
    """get_full_row's return type should be of instance table"""
    assert isinstance(test_row.get_full_row(subtable_title), Table)


def test_concatenate_tags_content(test_row):
    test_row._concatenate_tags_content(["test"])
