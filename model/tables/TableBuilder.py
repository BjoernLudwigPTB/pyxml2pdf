from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator
from PdfVisualisation.TableStyle import TableStyle
from model.tables.EventTable import EventTable


class TableBuilder:
    def __init__(self, properties, styles):
        self._styles = styles
        self._creator = Creator()
        self._prop = properties
        self._settings = self._parse_properties()
        self._table_styles = TableStyle()
        self._course = None
        self.create_subtables()

    def _parse_properties(self):
        """
        Extract all configuration information from properties file and set
        up a dict containing all this information. Later at least it will
        extract it... TODO extract actual information with something like
        settings = open(properties).read().split("\n")
        settings_dict = dict()

        :return list(list(str)): the dict with all configuration data out of
            properties file
        """
        properties = self._prop
        return [[
            'Wandern im Hoch - und Mittelgebirge', [
                'Hochgebirge', 'Mittelgebirge'], [
                'Wandern']], [
            'Klettern und Bouldern im Mittelgebirge', [
                'Mittelgebirge'], [
                'Klettern', 'Bouldern']], [
            'Ausbildung, Wandern und Klettern in Berlin', [
                ' in Berlin'], [
                'Ausbildung', 'Wandern', 'Klettern']], [
            'Mountainbiken', [
                'in Berlin', 'Hochgebirge', 'Mittelgebirge'], [
                'Mountainbiken']], [
            'Wandern im Hoch- und Mittelgebirge', [
                'Hochgebirge', 'Mittelgebirge'], [
                'Wandern']], [
            'Bergsteigen, Hochtouren und Klettern im Hochgebirge', [
                'Hochgebirge'], [
                'Bergsteigen', 'Hochtouren', 'Klettern']], [
            'Veranstaltungen für Familien', [
                'in Berlin', 'Hochgebirge', 'Mittelgebirge'], [
                'Familie']], [
            'Jugendgruppen und -events', [
                'in Berlin', 'Hochgebirge', 'Mittelgebirge'], [
                'Jugend']]]

    def create_subtables(self):
        """
        Create subtables for all different kinds of events.
        """

        for heading in self._settings:
            event_table = EventTable(heading[0], heading[1], heading[2])
            self.make_headers(heading[0])

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

    def make_headers(self, main_header):
        headers = [self._creator.create_table([[Paragraph(
            main_header, self._styles['Heading1'])]],
            self._table_styles.table_width,
            self._table_styles.heading)]
        headings = ['Art', 'Ort', 'Leitung', 'Beschreibung', 'Zielgruppe',
                    'Voraussetzungen', 'Bemerkungen']
        columns = []
        for heading in headings:
            columns.append(Paragraph(heading, self._styles['Heading2']))
        headers.append(self._creator.create_table_fixed(
            headings, self._table_styles.columm_widths,
            self._table_styles.sub_heading))
        return headers
