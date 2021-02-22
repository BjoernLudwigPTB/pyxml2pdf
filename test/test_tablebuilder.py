import pytest

from pyxml2pdf.tables.builder import TableBuilder


@pytest.fixture
def table_data():
    return ["f", "s", "t"]


@pytest.fixture
def table_builder():
    return TableBuilder()


def test_tablebuilder_fixedwidth_call(table_data, table_builder):
    """Check proper execution of create_fixedwidth_table"""
    table_builder.create_fixedwidth_table(table_data)


def test_property_subtables(table_builder):
    """Check property subtables existence and if something gets returned"""
    assert table_builder.subtables


def test_tablebuilder_distribute_row(test_row, table_builder):
    """Check proper execution of distribute_row"""
    table_builder.distribute_row(test_row)
