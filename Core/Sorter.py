class Sorter:
    # Taken from [http://effbot.org/zone/element-sort.htm
    # ](http://effbot.org/zone/element-sort.htm) and adapted.

    def __init__(self, doc, courses):
        self._doc = doc
        self._courses = courses

    def sort_parsed_xml(self, sort_key):
        from datetime import datetime

        def get_key(course):
            _key = course.findtext(sort_key)
            if _key:
                return datetime.strptime(_key, "%d.%m.%Y %H:%M")
            else:
                return datetime.strptime("01.01.2099 00:00", "%d.%m.%Y %H:%M")

        self._courses[:] = sorted(self._courses, key=get_key)
        return self._courses[:]
