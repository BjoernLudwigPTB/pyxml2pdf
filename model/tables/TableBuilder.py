from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator


class TableBuilder:
    def __init__(self, properties):
        self._creator = Creator()
        self._settings = open(properties).read().split("\n")
        self._course = None
        self._prop = properties

    def create_subtables(self):
        """
        Create subtables for all different kinds of events.

        TODO implement the parsing of properties/_settings and creation of
        tables for every heading.no_x
        """

        self.make_row(event, "heading.no1",
            self._table_style.heading, "     ", styles["Heading1"])

    def read_settings(self, description):
        """
        Find the desired entry from the properties file by its description.

        :param str description: this is the string for which to look in the
        contents
        :return str: this is the interpreted string
        """
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
