from typing import List

from reportlab.platypus import Table  # type:ignore


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

    title: str
    locations: List[str]
    activities: List[str]
    events: List[Table]

    def __init__(self, title, locations, activities):
        self.events = []
        self.title = title
        self.locations = locations
        self.activities = activities

    def append(self, event: Table):
        """Append an event to the end of the table

        :param event: a single event that should be
            appended to the table's list of events
        """
        self.events.append(event)

    def extend(self, event_list):
        """Append a a list of events to the end of the table

        :param event_list: a list of events that should be appended to the table's
            list of events
        """
        self.events.extend(event_list)
