"""This module contains the class :class:`Sorter` to sort the resulting table."""

from datetime import datetime


class Sorter:
    """Provides a method to sort from xml extracted data by a tag containing a date

    We took `effbot.org <http://effbot.org/zone/element-sort.htm>`_ and adapted the
    code to our needs of sorting a list of :py:class:`xml.etree.ElementTree.Element`
    by the texts of one of their tags containing a string representation of a date.

    :param List[xml.etree.ElementTree.Element] courses: rows that where extracted
        from an xml source
    """

    def __init__(self, courses):
        self._courses = courses

    def sort_parsed_xml(self, sort_key):
        """Sort a list of :py:class:`xml.etree.ElementTree.Element` by their date

        Taken from `effbot.org <http://effbot.org/zone/element-sort.htm>`_ and adapted.

        :param str sort_key: the XML tag which contains the data
        """

        def get_key(course):
            _key = course.findtext(sort_key)
            # Try to provide a reasonable sortable date string.
            try:
                if _key:
                    return datetime.strptime(_key, "%d.%m.%Y %H:%M")
                return datetime.strptime("01.01.2099 00:00", "%d.%m.%Y %H:%M")
            except ValueError:
                # If that did not work return the key itself.
                return _key

        self._courses[:] = sorted(self._courses, key=get_key)
        return self._courses[:]
