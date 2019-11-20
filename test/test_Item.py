from xml.etree.ElementTree import Element

import pytest

from Core.items import Item


def test_item_init():
    Item(Element("test"))


def test_collect_event_data_empty_call():
    parser = Item(Element("test"))
