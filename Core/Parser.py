import warnings
from typing import List

from reportlab.platypus.flowables import KeepTogether

from Core.events import Event
from model.tables.Creator import Creator
from model.tables.TableBuilder import TableBuilder


class Parser:
    """XML parser to extract all interesting information from xml input

    :param str properties: path to the properties file
    :param List[KeepTogether] elements: optional elements to populate the Parser
    """

    _elements: List[KeepTogether]
    _creator: Creator
    _table_manager: TableBuilder

    def __init__(self, properties, elements=[]):
        self._elements = elements
        self._creator = Creator()
        self._table_manager = TableBuilder(properties)

    def collect_xml_data(self, events):
        """Traverse the parsed xml data and gather collected event data

        The collected xml data then is passed to the table_manager and all arranged
        data is return.

        :param List[Event] events: a list of the items from which the texts shall be
            extracted into a nicely formatted table
        :returns List[KeepTogether]: list of all table rows containing the relevant
            event data
        """
        if events is not None:
            for event in events:
                event = Event(event)
                self._table_manager.distribute_event(event)
            subtable_elements = self._table_manager.collect_subtables()
            for subtable_element in subtable_elements:
                self._elements.append(KeepTogether(subtable_element))
            return self._elements
        else:
            warnings.warn("There were no items to print.", RuntimeWarning)
