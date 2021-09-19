"""A wrapper :py:class:`pyxml2pdf.core.events.Event` for xml extracted data"""
import re
from typing import List, Type

import defusedxml  # type: ignore
from pyxml2pdf.core.rows import XMLCell, XMLRow
from pyxml2pdf.styles.table_styles import XMLTableStyle
from pyxml2pdf.tables.builder import TableBuilder
from reportlab.platypus import Table  # type: ignore

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
    _reduced_row: Table
    _date: str
    _responsible: str
    _reduced_columns: List[XMLCell]
    _cell_styler: Type[XMLCell]

    def __init__(self, element):
        # Initialize definitely needed instance variables.
        self._date = self._responsible = ""
        # Call XMLRow constructor
        super().__init__(element)
        self._date = self._init_date()
        self._responsible = self._concatenate_tags_content(["Kursleiter"])
        self._reduced_columns = self._init_full_row()

    def _init_reduced_row(self, subtable_title):
        """Initializes the reduced version of the event

        Create a table row in proper format but just containing a brief description
        of the event and a reference to the fully described event at another place,
        namely the subtable with the given title.

        :param str subtable_title: title of the subtable which contains the full event

        .. warning:: Do not call this function directly since it is automatically
            called right after :meth:`get_full_row` is invoked.
        """
        self._reduced_columns.append(
            self._cell_styler(self._build_description(link=subtable_title))
        )
        self._reduced_row = self._table_builder.create_fixedwidth_table(
            [self._reduced_columns],
            self._table_style.column_widths[:4]
            + [sum(self._table_style.column_widths[4:])],
        )

    def create_reduced_after_full(func):
        """Decorator to execute :meth:`_init_reduced_row` with :meth:`get_full_row`

        :returns: the return value of :meth:`get_full_row`
        :rtype: Table
        """

        def execute_get_full_and_init_reduced_row(self, *args, **kwargs):
            """Exchange a table row with all the event's information against a
            subtable's title

            This ensures, that after handing over the full information, the reduced
            version with a reference to the subtable containing the full version is
            created.

            .. note:: This is ensured by a decorator, which is why the function
                signature on `ReadTheDocs.org
                <https://pyxml2pdf.readthedocs.io/en/latest/pyxml2pdf.html#core.events
                .Event.get_full_row>`_ is displayed incorrectly. The parameter and
                return value are as follows...

            :param str subtable_title: the title of the subtable in which the row will
                be integrated
            :returns: a table row with all the event's information
            :rtype: Table
            """
            return_table = func(self, *args, **kwargs)
            self._init_reduced_row(args[0])
            return return_table

        return execute_get_full_and_init_reduced_row

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

        extracted_dates = [
            self._concatenate_tags_content(date)
            for date in dates
            if self._concatenate_tags_content(date)
        ]
        extracted_dates = "<br/>und<br/>".join(extracted_dates)

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

    @create_reduced_after_full
    def get_full_row(self, subtable_title: str = None) -> Table:
        """Exchange a table row with all the event's information against a
        subtable's title

        This ensures, that after handing over the full information, the reduced
        version with a reference to the subtable containing the  full version is
        created.

        .. note:: This is ensured by a decorator, which is why the function
            signature on `ReadTheDocs.org
            <https://pyxml2pdf.readthedocs.io/en/latest/pyxml2pdf.html#core.events
            .Event.get_full_row>`_ is displayed incorrectly. The parameter and
            return value are as follows...

        :param subtable_title: the title of the subtable in which the row will
            be integrated
        :returns: a table row with all the event's information
        """
        return self._full_row

    @property
    def responsible(self):
        """Return the name of the person being responsible for the event

        :returns: first and last name
        :rtype: str
        """
        return self._responsible

    @property
    def identifier(self):
        """Return the identifier of the event

        :returns: identifier
        :rtype: str
        """
        return self._date

    def get_table_row(self, subtable_title):
        """Return the table row representation of the event

        This is the API of :py:class:`pyxml2pdf.core.events.Event` for getting the
        table row
        representation of the event. It makes sure, that on the first call
        :meth:`get_full_row` is invoked and otherwise
        :attr:`pyxml2pdf.core.events.Event._reduced_row` is returned.

        :param str subtable_title: the title of the subtable in which the row will
            be integrated
        :returns: a table row representation of the event
        :rtype: Table
        """
        # We check if the reduced row was produced before, which means in turn,
        # that :meth:`get_table_row` was called at least once before. Otherwise we call
        # :meth:`get_full_row` which automatically triggers the creation of the
        # reduced row for later uses.
        try:
            return self._reduced_row
        except AttributeError:
            return self.get_full_row(subtable_title)
