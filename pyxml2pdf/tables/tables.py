from typing import List

from reportlab.platypus import Table  # type:ignore


class EventTable:
    """An :class:`EventTable` contains a subset of the xml inputs

    Contains all events which cover the mentioned activities at the
    mentioned locations. Every event listed covers at least one of the
    listed activities at one of the listed locations.

    :param str title: Name of the table
    :param str locations: List of locations where the activities take place
    :param str activities: List of activities covered by the listed events
    """

    def __init__(self, title: str, locations: List[str], activities: List[str]):
        """Initialize a table containing a subset of the XML data"""
        self.events = []
        self.title = title
        self.locations: List[str] = locations
        self.activities = activities

    def append(self, event: Table):
        """Append an event to the end of the table

        :param event: a single event that should be appended to the table
        """
        self.events.append(event)

    def extend(self, event_list: List[Table]):
        """Append a a list of events to the end of the table

        :param event_list: a list of events that should be appended to the table's
            list of events
        """
        self.events.extend(event_list)

    @property
    def events(self) -> List[Table]:
        """List[Table]: The list of events as Table objects"""
        return self._events

    @events.setter
    def events(self, value: List[Table]):
        self._events = value

    @property
    def title(self) -> str:
        """str: Name of the table"""
        return self._title

    @title.setter
    def title(self, value: str):
        self._title = value

    @property
    def activities(self) -> List[str]:
        """List[str]: List of activities covered by the listed events"""
        return self._activities

    @activities.setter
    def activities(self, value: List[str]):
        self._activities = value

    @property
    def locations(self) -> List[str]:
        """List[str]: List of locations where the activities take place"""
        return self._locations  # type: List[str]

    @locations.setter
    def locations(self, value: List[str]):
        self._locations = value
