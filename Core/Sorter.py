class Sorter:
    """Sort a list of :py:mod:`xml.etree.ElementTree.Element` by their date

    Taken from `effbot.org <http://effbot.org/zone/element-sort.htm>`_ and adapted.

    :param List[xml.etree.ElementTree.Element]: events that where extracted from an xml
        source
    """

    def __init__(self, courses):
        self._courses = courses

    def sort_parsed_xml(self, sort_key):
        """Sort a list of :py:mod:`xml.etree.ElementTree.Element` by their date

        Taken from `effbot.org <http://effbot.org/zone/element-sort.htm>`_ and adapted.

        :param str sort_key: the xml tag which contains the data
        """
        from datetime import datetime

        def get_key(course):
            _key = course.findtext(sort_key)
            if _key:
                return datetime.strptime(_key, "%d.%m.%Y %H:%M")
            else:
                return datetime.strptime("01.01.2099 00:00", "%d.%m.%Y %H:%M")

        self._courses[:] = sorted(self._courses, key=get_key)
        return self._courses[:]
