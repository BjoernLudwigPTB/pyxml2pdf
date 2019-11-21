from typing import List

from reportlab.platypus import Table


class EventTable:

    _title: str
    _locations: List[str]
    _activities: List[str]
    _elements: List[Table]

    def __init__(self, title, locations, activities):
        """
        Contains all events which cover the mentioned activities at the
        mentioned locations. Every event listed covers at least one of the
        listed activities at one of the listed locations.

        :param str title: name of the table describing where and what is done in
            the included events
        :param List[str] locations: list of locations where the listed activities take
            place
        :param List[str] activities: list of activities covered by the listed
            events
        """
        self._elements = []
        self._title = title
        self._locations = locations
        self._activities = activities

    def append(self, event):
        """Append an event to the end of the table

        :param reportlab.platypus.Table event:
        """
        self._elements.append(event)

    def get_elements(self):
        """Return the whole item table

        :return list[reportlab.platypus.Table]: a list of all table rows
            containing the relevant event data
        """
        return self._elements

    def get_activities(self):
        """Return the activities shown in the event table

        :return list[str]: a list of all activities
        """
        return self._activities

    def get_locations(self):
        """Return the locations at which the events of this table take place

        :return list[str]: a list of all locations
        """
        return self._locations
