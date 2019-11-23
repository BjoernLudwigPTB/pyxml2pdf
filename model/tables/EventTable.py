from typing import List

from reportlab.platypus import Table


class EventTable:
    """An EventTable contains a subset of the xml inputs

    Contains all events which cover the mentioned activities at the
    mentioned locations. Every event listed covers at least one of the
    listed activities at one of the listed locations.

    :param str title: name of the table describing where and what is done in
        the included events
    :param List[str] locations: list of locations where the activities take place
    :param List[str] activities: list of activities covered by the listed events
    """

    _title: str
    _locations: List[str]
    _activities: List[str]
    _events: List[Table]

    def __init__(self, title, locations, activities):
        self._events = []
        self._title = title
        self._locations = locations
        self._activities = activities

    def append(self, event):
        """Append an event to the end of the table

        :param reportlab.platypus.Table event:
        """
        self._events.append(event)

    def events(self):
        """Return the whole item table

        :returns list[reportlab.platypus.Table]: a list of all table rows
            containing the relevant event data
        """
        return self._events

    def activities(self):
        """Return the activities shown in the event table

        :returns list[str]: a list of all activities
        """
        return self._activities

    def locations(self):
        """Return the locations at which the events of this table take place

        :returns list[str]: a list of all locations
        """
        return self._locations

    def title(self):
        """Return the title of the subtable

        :returns str: the title
        """
        return self._title
