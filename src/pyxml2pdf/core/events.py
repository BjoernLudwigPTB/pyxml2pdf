"""A wrapper :py:class:`pyxml2pdf.core.events.Event` for xml extracted data"""
import re
from typing import List

import defusedxml  # type: ignore
from reportlab.platypus import Table  # type: ignore

from pyxml2pdf.core.rows import XMLCell, XMLRow
from pyxml2pdf.styles.table_styles import XMLTableStyle
from pyxml2pdf.tables.builder import TableBuilder

# Monkeypatch standard library xml vulnerabilities.
defusedxml.defuse_stdlib()

__all__ = ["Event"]


class Event(XMLRow):
    """A specialisation of :class:`XMLRow` onto events from an ACB event program

    :param xml.etree.ElementTree.Element element: the element to build the instance from
    """

    _table_builder: TableBuilder = TableBuilder()
    _table_style: XMLTableStyle = XMLTableStyle()

    _categories: List[str]
    _full_row: Table
    _date: str
    _responsible: str

    def __init__(self, element):
        # Initialize definitely needed instance variables.
        self._date = self._responsible = ""
        # Call XMLRow constructor
        super().__init__(element)
        self._date = self._init_date()
        self._responsible = self._concatenate_tags_content(["Kursleiter"])

    def _init_full_row(self) -> List[XMLCell]:
        """Initialize the single table row containing all information of the event

        Extract interesting information from events children tags and connect them
        into a nicely formatted row of a table.

        :return: the common starting columns of any table representation
        :rtype: List[XMLCell]
        """
        table_columns = [
            self._cell_styler(self._build_type()),
            self._cell_styler(self._date),
            self._cell_styler(self._concatenate_tags_content(["Ort1"])),
            self._cell_styler(self._responsible),
            self._cell_styler(
                self._build_description(self._concatenate_tags_content(["TrainerURL"]))
            ),
            self._cell_styler(self._concatenate_tags_content(["Zielgruppe"])),
            self._cell_styler(
                self._parse_prerequisites(
                    self._concatenate_tags_content(["Voraussetzung"]),
                    self._concatenate_tags_content(["Ausruestung"]),
                    self._concatenate_tags_content(["Kurskosten"]),
                    self._concatenate_tags_content(["Leistungen"]),
                )
            ),
        ]
        self._full_row = self._table_builder.create_fixedwidth_table([table_columns])
        return table_columns[:4]

    @staticmethod
    def _remove_century(four_digit_year):
        """Remove the first two digits of the string representing the year

        :param typing.Match four_digit_year: the result of :py:meth:`re.sub`
        :return: the last two digits of the string representing the year
        :rtype: str
        """
        return four_digit_year.group(0)[2:]

    def _init_date(self):
        """Create a properly formatted string containing the identifier of the event"""
        # Extract data from xml children tags' texts. Since the date can consist of
        # three date ranges, we concatenate them separated with a line containing
        # only an "und".

        dates = [
            ["TerminDatumVon1", "TerminDatumBis1"],
            ["TerminDatumVon2", "TerminDatumBis2"],
            ["TerminDatumVon3", "TerminDatumBis3"],
        ]

        raw_dates: List[str] = [
            self._concatenate_tags_content(date)
            for date in dates
            if self._concatenate_tags_content(date)
        ]
        extracted_dates: str = "<br/>und<br/>".join(raw_dates)

        # Replace any extracted_dates of a form similar to 31.12.2099 with "on request".
        if "2099" in extracted_dates:
            new_date = "auf Anfrage"
        else:
            # Remove placeholders for missing time specifications and the first two
            # digits of the year specification.
            new_date = re.sub(
                "[0-9]{4,}", self._remove_century, extracted_dates.replace("00:00", "")
            )
        return new_date

    @staticmethod
    def _parse_prerequisites(
        personal: str, material: str, financial: str, offers: str
    ) -> str:
        """
        Determine all prerequisites and assemble a string accordingly.

        :param str material: material prerequisite xml text
        :param str personal: personal prerequisite xml text
        :param str financial: financial prerequisite xml text
        :param str offers: xml text of what is included in the price
        :returns: the text to insert in prerequisite column
            the current event
        :rtype: str
        """
        if not personal:
            personal = "keine"
        if not material:
            material = "keine"
        if not financial:
            financial = "0,00"
        if offers:
            offers = offers.join([" (", ")"])

        return "<br/>".join(
            [
                "".join(["a) ", personal]),
                "".join(["b) ", material]),
                "".join(["c) ", financial, " €", offers]),
            ]
        )

    def _build_description(self, link: str = "") -> str:
        """Build the description for the event

        This covers all cases with empty texts in some of the according children tags
        and the full as well as the reduced version with just the reference to the
        subtable where the full version can be found. Since the title of the event is
        mandatory, and the beginning of the description is always filled by the same
        tags' texts those are not received as parameter but directly retrieved from the
        xml data.

        :param str link: a link to more details like the trainer url or the subtable
        :returns: the full description including url if provided
        :rtype: str
        """
        texts = [
            self._concatenate_tags_content(["Bezeichnung"]).join(["<b>", "</b>"]),
            self._concatenate_tags_content(["Bezeichnung2"]),
            self._concatenate_tags_content(["Beschreibung"]),
        ]
        full_description = " – ".join([text for text in texts if text])
        if link:
            joiner = "." if full_description[-1] != "." else ""
            full_description = joiner.join(
                [full_description, link.join([" Mehr Infos unter <b><i>", "</i></b>."])]
            )

        return full_description

    def _build_type(self) -> str:
        """Build the type for the event

        This assembles the type of the event from the different kinds.

        :returns: the entry in the type column of the event
        :rtype: str
        """
        types = self._concatenate_tags_content(["Kursart"])
        types = types.replace("Gemeinschaftsfahrt", "Eigenverant- wortlich")

        return types

    @property
    def responsible(self) -> str:
        """Return the name of the person being responsible for the event

        :returns: first and last name
        :rtype: str
        """
        return self._responsible

    @property
    def identifier(self) -> str:
        """Return the date as an identifier of the event

        :returns: date
        :rtype: str
        """
        return self._date
