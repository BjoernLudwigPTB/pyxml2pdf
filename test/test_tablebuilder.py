import pytest

from pyxml2pdf.model.tables.TableBuilder import TableBuilder


@pytest.fixture
def table_data():
    return ["f", "s", "t"]


@pytest.fixture
def table_builder():
    return TableBuilder()


def test_tablebuilder_fixedwidth_call(table_data, table_builder):
    table_builder.create_fixedwidth_table(table_data)
