import pytest

from Core.Parser import Parser


def test_collect_xml_data_empty_call():
    parser = Parser("test")
    with pytest.warns(RuntimeWarning):
        parser.collect_xml_data(events=None)


def test_collect_event_data_empty_call():
    parser = Parser("test")
    with pytest.warns(RuntimeWarning):
        parser.collect_event_data(event=None)
