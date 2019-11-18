import warnings
from typing import List

from reportlab.platypus import Paragraph

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator
from model.tables.EventTable import EventTable


class TableBuilder:
    def __init__(self, properties, styles):
        self._styles = styles
        self._creator = Creator()
        self._prop = properties
        self._subtable_names_and_categs = self._parse_properties()
        self._table_styles = TableStyle()
        self._subtables = self.create_subtables()

    @staticmethod
    def _parse_properties():
        """
        Extract all configuration information from properties file and set
        up a dict containing all this information. Later at least it will
        extract it.

        :returns: the list with all configuration data out of properties file
        :rtype: List[List[Union[str, List[str]]]]
        """

        klettern = [
            "Klettern und Bouldern im Mittelgebirge",
            ["Mittelgebirge"],
            ["Klettern", "Bouldern"],
        ]
        wandern = [
            "Wandern im Hoch - und Mittelgebirge",
            ["Hochgebirge", "Mittelgebirge"],
            ["Wandern"],
        ]
        mountainbiken = ["Mountainbiken", ["Mountainbiken"], ["Mountainbiken"]]
        ausbildung = [
            "Ausbildung, Wandern und Klettern in Berlin",
            ["in Berlin"],
            ["Grundlagenkurs", "Wandern", "Klettern"],
        ]
        bergsteigen = [
            "Ski, Bergsteigen, Hochtouren und Klettern im Hochgebirge",
            ["Hochgebirge"],
            ["Bergsteigen", "Hochtouren", "Höhle", "Klettern", "Klettersteig", "Ski"],
        ]
        familie = ["Veranstaltungen für Familien", ["Familie"], ["Familie"]]
        jugend = ["Jugendgruppen und -events", ["Jugend"], ["Jugend"]]

        return [
            familie,
            ausbildung,
            wandern,
            mountainbiken,
            bergsteigen,
            jugend,
            klettern,
        ]

    def create_subtables(self):
        """
        Create subtables for all different kinds of items.

        :return list[EventTable]: a list of all subtables
        """

        subtables = []
        for subtables_props in self._subtable_names_and_categs:
            subtable = EventTable(
                subtables_props[0], subtables_props[1], subtables_props[2]
            )
            headers = self.make_header(subtables_props[0])
            for header in headers:
                subtable.add_event(header)
            subtables.append(subtable)
        return subtables

    def make_header(self, title):
        """ Build the first two rows of a subtable

        Build the first two rows of a subtable with its title and column headings taken
        from the properties file.

        :param str title: the title of the subtable
        :returns: two line table with title and headings
        :rtype: List[reportlab.platypus.Table]
        """
        # Create first row spanning the full width and title as content.
        title_row = [
            self._creator.create_fixedwidth_table(
                [[Paragraph(title, self._styles["Heading1"])]],
                self._table_styles.table_width,
                self._table_styles.heading,
            )
        ]

        # These are the column headings that should be populated from the
        # properties-file.
        headings = [
            "Art",
            "Datum",
            "Ort",
            "Leitung",
            "Beschreibung",
            "Zielgruppe",
            "Voraussetzungen<br/>a) persönliche | b) " "materielle | c) finanzielle",
        ]

        # Create row containing one column per heading.
        columns = []
        for heading in headings:
            columns.append(Paragraph(heading, self._styles["Heading2"]))

        # Concatenate both rows.
        title_row.append(
            self._creator.create_fixedwidth_table(
                [columns],
                self._table_styles.get_column_widths(),
                self._table_styles.sub_heading,
            )
        )
        return title_row

    def collect_subtables(self):
        aggregated_subtables = []
        for table in self._subtables:
            for element in table.get_elements():
                aggregated_subtables.append(element)
        return aggregated_subtables

    def distribute_event(self, event_as_tablerow, categories):
        """
        Distribute an event to the subtables according to the related categories.

        :param reportlab.platypus.Table event_as_tablerow: event which is to be
            distributed
        :param List[str] categories: the categories list of the specified event
        """
        distribution_failed = True
        set_of_cats = set(categories)
        for subtable in self._subtables:
            _locations = subtable.get_locations()
            _activities = subtable.get_activities()
            if set_of_cats.intersection(_activities):
                if set_of_cats.intersection(_locations):
                    subtable.add_event(event_as_tablerow)
                    distribution_failed = False
        if distribution_failed:
            warnings.warn(
                event_as_tablerow.__getattribute__("_cellvalues")[0][3].text
                + "'s event on "
                + event_as_tablerow.__getattribute__("_cellvalues")[0][1].text
                + " would not be printed, because it does not contain a valid "
                "combination of locations and activities. Either add a valid location "
                "or add a valid activity or both.",
                RuntimeWarning,
            )
