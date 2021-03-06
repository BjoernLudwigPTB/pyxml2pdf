import warnings
from typing import List, Optional, Tuple, Union

from reportlab.platypus import Flowable, Paragraph, Table

from pyxml2pdf.model.tables.EventTable import EventTable
from pyxml2pdf.PdfVisualisation.TableStyle import TableStyle


class TableBuilder:
    def __init__(self):
        self._subtable_names_and_categs = self._parse_properties()
        self._table_style = TableStyle()
        self._styles = self._table_style.custom_styles
        self._subtables = self.create_subtables()

    @staticmethod
    def _parse_properties() -> List[List[Union[str, List[str]]]]:
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
            ["Klettern", "Bouldern", "Höhle"],
        ]
        wandern = [
            "Wandern im Hoch - und Mittelgebirge",
            ["Hochgebirge", "Mittelgebirge"],
            ["Wandern"],
        ]
        mountainbiken = ["Mountainbiken", ["Mountainbiken"], ["Mountainbiken"]]
        bergsteigen = [
            "Ski, Bergsteigen, Hochtouren und Klettern im Hochgebirge",
            ["Hochgebirge"],
            ["Bergsteigen", "Hochtouren", "Höhle", "Klettern", "Klettersteig", "Ski"],
        ]
        familie = ["Veranstaltungen für Familien", ["Familie"], ["Familie"]]
        jugend = ["Jugendgruppen und -events", ["Jugend"], ["Jugend"]]

        return [
            familie,
            bergsteigen,
            jugend,
            klettern,
        ]

    def create_subtables(self) -> List[EventTable]:
        """Create subtables for all different kinds of events

        :return List[EventTable]: a list of all subtables
        """

        subtables = []
        for subtables_props in self._subtable_names_and_categs:
            subtable = EventTable(
                subtables_props[0], subtables_props[1], subtables_props[2]
            )
            headers = self.make_header(subtables_props[0])
            for header in headers:
                subtable.append(header)
            subtables.append(subtable)
        return subtables

    def make_header(self, title: str) -> List[Table]:
        """Build the first two rows of a subtable

        Build the first two rows of a subtable with its title and column headings taken
        from the properties file.

        :param str title: the title of the subtable
        :returns: two line table with title and headings
        :rtype: List[reportlab.platypus.Table]
        """
        # Create first row spanning the full width and title as content.
        title_row = [
            self.create_fixedwidth_table(
                [[Paragraph(title, self._styles["Heading1"])]],
                self._table_style.table_width,
                self._table_style.heading,
            )
        ]

        # These are the column headings that should be populated from the
        # properties-file.
        headings = [
            "Charakter",
            "Datum",
            "Ort",
            "Leitung",
            "Beschreibung",
            "Zielgruppe",
            "Voraussetzungen<br/>a) persönliche | b) " "materielle | c) finanzielle",
        ]

        # Create row containing one column per heading.
        columns = [Paragraph(heading, self._styles["Heading2"]) for heading in headings]

        # Concatenate both rows.
        title_row.append(
            self.create_fixedwidth_table(
                [columns],
                self._table_style.column_widths,
                self._table_style.sub_heading,
            )
        )
        return title_row

    def collect_subtables(self) -> List[Table]:
        """Collect all subtables at once

        :return: the subtables
        """
        return [element for subtable in self._subtables for element in subtable.events]

    def distribute_event(self, event):
        """Distribute an event to the subtables according to the related categories

        :param Core.events.Event event: event to distribute
        """
        distribution_failed = True
        set_of_cats = set(event.categories)
        for subtable in self._subtables:
            if set_of_cats.intersection(
                subtable.activities
            ) and set_of_cats.intersection(subtable.locations):
                subtable.append(event.get_table_row(subtable.title))
                distribution_failed = False
        if distribution_failed:
            warnings.warn(
                event.responsible
                + "'s event on "
                + event.date
                + " would not be printed, because it does not contain a valid"
                " combination of locations and activities. Currently it contains "
                + str(event.categories)
                + ". Either add a valid location or add a valid activity or both.",
                RuntimeWarning,
            )

    def create_fixedwidth_table(
        self,
        cells: List[List[Flowable]],
        widths: Optional[Union[float, List[float]]] = None,
        style: Optional[List[Tuple[Union[str, Tuple[int]]]]] = None,
    ) -> Table:
        """Create a table with specified column widths

        Create a table from specified cells with fixed column widths and a specific
        style.

        :param cells: cells wrapped by a list representing the columns wrapped by a
            list representing the lines
        :param widths: Optional column widths. The default results in reasonable
            settings based on experience.
        :param style: Optional table's style. The default results in reasonable
            settings based on experience.
        :returns: A table containing specified cells in fixed width, styled columns.
        """
        if widths is None:
            widths = self._table_style.column_widths
        if style is None:
            style = self._table_style.normal
        table = Table(cells, colWidths=widths)
        table.setStyle(style)

        return table
