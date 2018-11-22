from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator


class CourseBuilder:
    def __init__(self, properties):
        self._creator = Creator()
        self._settings = open(properties).read().split("\n")
        self._course = None
        self._prop = properties

    def pick_course(self, path, name, task):
        module = __import__(path, fromlist=[name])
        class_ = getattr(module, name)(task, self._prop)
        self._course = class_

    def run(self):
        return self._course.make_course()

    def read_settings(self, description):
        if not description:
            return description
        for elem in self._settings:
            if description in elem:
                desc = elem.split("=")
                print("\n--------------------------------")
                print("FOUND!   " + desc.__str__())
                print("--------------------------------\n")
                return desc[1]

        print("\n--------------------------------")
        print("NOT FOUND!")
        print("--------------------------------\n")
        return description

    def make_row(self, elements, group, attrib, table_style, to_logs, styles):
        if group.attrib:
            check = self.read_settings(group.get(attrib))
            if check:
                desc = [[Paragraph(check, styles)]]
                print(to_logs + group.get(attrib) + "  =  " + desc[0][0].text)

                row = self._creator.create_table(desc, 8.0, table_style)
                elements.append(row)
