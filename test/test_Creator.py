import pytest

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator


@pytest.fixture()
def table_data():
    table_style = TableStyle()
    return ["f", "s", "t"], [1, 2, 3], table_style.normal


def test_creator_call(table_data):
    creator = Creator()
    creator.create_fixedwidth_table(table_data[0], table_data[1], table_data[2])
