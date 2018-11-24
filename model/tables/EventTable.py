from reportlab.lib.styles import getSampleStyleSheet

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Table import Table


class EventTable(Table):

    def __init__(self, name, activities, locations):
        """
        Contains all events which cover the mentioned activities at the
        mentioned locations. Every event listed covers at least one of the
        listed activities at one of the listed locations.

        :param str name: name of the table describing where and what is done in
            the included events
        :param list(str) activities: list of activities covered by the listed
            events
        :param list(str) locations: list of locations at one of which all
            listed activities take place
        :return str: the table itself
        course
        """
        self._name = name
        self._activities = activities
        self._locations = locations
        return self

    def add_event(self):
        """
        Adds a single event to the table later to be displayed as part of the
        table.
        TODO implement
        """
        pass

    def make_course(self):
        styles = getSampleStyleSheet()
        table_style = TableStyle()

        for argument in self._course:
            self.add_attribute(argument)

        self.create_visualisation(styles["Italic"])

        self.resize_table()

        row = self._creator.create_table_fixed(
            self._desc_courses, self._active_objects, table_style.normal)
        return row
