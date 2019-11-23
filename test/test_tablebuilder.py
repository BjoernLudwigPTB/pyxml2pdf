import pytest

from PdfVisualisation.TableStyle import TableStyle
from model.tables.TableBuilder import TableBuilder


@pytest.fixture()
def table_data():
    table_style = TableStyle()
    return ["f", "s", "t"], [1, 2, 3], table_style.normal


def test_tablebuilder_fixedwidth_call(table_data):
    TableBuilder.create_fixedwidth_table(table_data[0], table_data[1], table_data[2])
