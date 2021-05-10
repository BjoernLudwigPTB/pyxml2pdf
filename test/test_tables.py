from typing import Callable, List

import pytest
from hypothesis import given, HealthCheck, settings, strategies as hst

from input.properties import subtable_settings  # type: ignore
from pyxml2pdf.core.types import SubtableSetting  # type: ignore
from pyxml2pdf.tables.tables import XMLTable


@pytest.fixture
def test_table_settings() -> SubtableSetting:
    return subtable_settings[0]


@pytest.fixture
def test_table(test_table_settings) -> XMLTable:
    return XMLTable(test_table_settings.label, test_table_settings.include)


def test_xmltable_init(test_table):
    assert isinstance(test_table.include_filters, List)
    for filter in test_table.include_filters:
        assert isinstance(filter, List)
    assert isinstance(test_table.rows, List)
    assert isinstance(test_table.title, str)
    assert isinstance(test_table.append, Callable)
    assert isinstance(test_table.extend, Callable)


def test_xmltable_set_and_get_rows(test_table, test_row):
    """Check if a list of one row can be appended."""
    assert test_table.rows == []
    test_table.rows = [test_row.get_table_row(test_table.title)]
    assert test_table.rows


@settings(suppress_health_check=(HealthCheck.function_scoped_fixture,))
@given(title=hst.text())
def test_xmltable_set_and_get_title(test_table, title):
    """Check if a list of one row can be appended."""
    test_table.title = title
    assert test_table.title == title


@settings(suppress_health_check=(HealthCheck.function_scoped_fixture,))
@given(filters=hst.lists(elements=hst.lists(hst.text()), min_size=1))
def test_xmltable_set_and_get_filters(test_table, filters):
    """Check if a list of one row can be appended."""
    assert test_table.include_filters
    test_table.include_filters = filters
    assert test_table.include_filters == filters


def test_xmltable_append(test_table, test_row):
    """Check if a row can be appended."""
    test_table.append(test_row.get_table_row(test_table.title))
    assert test_table.rows[-1] == test_row.get_table_row(test_table.title)


def test_xmltable_extend(test_table, test_row):
    """Check if a list of one row can be appended."""
    test_table.extend([test_row.get_table_row(test_table.title)])
    assert test_table.rows[-1] == test_row.get_table_row(test_table.title)
