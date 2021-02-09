import pytest

from pyxml2pdf.core.parser import Parser


def test_collect_xml_data_empty_call():
    """Parser should warm us if data will not be printed, because it lacks content"""
    with pytest.raises(TypeError):
        Parser()
