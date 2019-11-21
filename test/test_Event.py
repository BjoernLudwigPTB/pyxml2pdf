from xml.etree.ElementTree import Element

from Core.events import Event


def test_item_init():
    Event(Element("test"))


def test_collect_event_data_empty_call():
    parser = Event(Element("test"))
