import warnings
from typing import List, Optional, Tuple, Union

from reportlab.platypus import Flowable, Paragraph, Table  # type: ignore

from input.properties import columns, subtables  # type: ignore
from pyxml2pdf.styles.table_styles import TableStyle
from pyxml2pdf.tables.tables import EventTable


class TableBuilder:
    def __init__(self):
        self._table_style = TableStyle()
        self._stylesheet = self._table_style.custom_styles["stylesheet"]
        self._subtables = self.create_subtables()

    def create_subtables(self):
        """Create subtables for all different kinds of events

        :return List[EventTable]: a list of all subtables
        """
        subtables_list = []
        for subtable in subtables:
            subtable_table = EventTable(
                subtable["label"], subtable["content"][0], subtable["content"][1]
            )
            subtable_table.extend(self.make_header(subtable["label"]))
            subtables_list.append(subtable_table)
        return subtables_list

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
                [[Paragraph(title, self._stylesheet["Heading1"])]],
                self._table_style.table_width,
                self._table_style.custom_styles["heading"],
            )
        ]

        # Create row containing one column per heading.
        columns_list = [
            Paragraph(heading, self._stylesheet["Heading2"])
            for heading in [column["label"] for column in columns]
        ]

        # Concatenate both rows.
        title_row.append(
            self.create_fixedwidth_table(
                [columns_list],
                self._table_style.column_widths,
                self._table_style.custom_styles["sub_heading"],
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
            style = self._table_style.custom_styles["normal"]
        table = Table(cells, colWidths=widths)
        table.setStyle(style)

        return table
