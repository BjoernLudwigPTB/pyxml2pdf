"""Module to provide a wrapper :py:class:`Core.events.Event` for xml extracted data"""
import re
from typing import List, Match
from xml.etree.ElementTree import Element

from reportlab.platypus import Paragraph, Table

from pyxml2pdf.model.tables.TableBuilder import TableBuilder
from pyxml2pdf.PdfVisualisation.TableStyle import TableStyle

__all__ = ["Event"]


class Event(Element):
    """A wrapper class for :py:class:`xml.etree.ElementTree.Element`

    :py:class:`xml.etree.ElementTree.Element` is augmented with the table row
    representation and the attributes and methods to manipulate everything
    according to the final tables needs. A :py:class:`Core.events.Event` can only
    be initialized with an object of type :py:class:`xml.etree.ElementTree.Element`.

    :param xml.etree.ElementTree.Element element: the element to build the instance from
    """

    class EventParagraph(Paragraph):
        """A wrapper class for :py:class:`reportlab.platypus.Paragraph`

        :py:class:`reportlab.platypus.Paragraph` is solely used with one
        certain style, which is handed over in the constructor.

        :param str text: the text to write into row
        """

        def __init__(self, text: str):
            super().__init__(text, self.style)

    _table_builder: TableBuilder = TableBuilder()
    _table_style: TableStyle = TableStyle()

    _categories: List[str]
    _full_row: Table
    _reduced_row: Table
    _date: str
    _responsible: str
    _reduced_columns: List[EventParagraph]

    def __init__(self, element):
        # Call Element constructor and extend ourselves by extending all children
        # tags to create an underlying copy of element.
        super().__init__(element.tag, element.attrib)
        self.extend(list(element))
        # Initialize needed objects especially for table creation.
        self.EventParagraph.style = self._table_style.custom_styles["Normal"]
        # Initialize definitely needed instance variables.
        self._init_categories()
        self._date = self._init_date()
        self._responsible = self._concatenate_tags_content(["Kursleiter"])
        self._reduced_columns = self._init_full_row()

    def _init_categories(self):
        """Initialize the list of categories from the according xml tag's content"""
        categories: str = self._concatenate_tags_content(["Kategorie"])
        self._categories = categories.split(", ")

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
            self.EventParagraph(self._build_description(link=subtable_title))
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
            version with a reference to the subtable containing the  full version is
            created.

            .. note:: This is ensured by a decorator, which is why the function
                signature on `ReadTheDocs.org
                <https://pyxml2pdf.readthedocs.io/en/latest/pyxml2pdf.html#Core.events
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

    def _concatenate_tags_content(self, event_subelements, separator=" - "):
        """Form one string from the texts of a subset of an event's children tags

        Form a string of the content for all desired event children tags by
        concatenating them together with a separator. This is especially necessary,
        since :py:mod:`reportlab.platypus.Paragraph` cannot handle `None`s as texts but
        handles as well the concatenation of XML tags' content, if `event_tags` has more
        than one element.

        :param List[str] event_subelements: list of all tags for which the
            descriptive texts is wanted, even if it is just one
        :param str separator: the separator in between the concatenated texts
        :returns: concatenated, separated texts of all tags for the current event
        :rtype: str
        """
        return separator.join(
            [self.findtext(tag) for tag in event_subelements if self.findtext(tag)]
        )

    def _init_full_row(self) -> List[EventParagraph]:
        """Initialize the single table row containing all information of the event

        Extract interesting information from events children tags and connect them
        into a nicely formatted row of a table.

        :return: the common starting columns of any table representation
        """
        table_columns = [
            self.EventParagraph(self._concatenate_tags_content(["Kursart"])),
            self.EventParagraph(self._date),
            self.EventParagraph(self._concatenate_tags_content(["Ort1"])),
            self.EventParagraph(self._responsible),
            self.EventParagraph(
                self._build_description(self._concatenate_tags_content(["TrainerURL"]))
            ),
            self.EventParagraph(self._concatenate_tags_content(["Zielgruppe"])),
            self.EventParagraph(
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
    def _remove_century(matchobj: Match) -> str:
        """Remove the first two digits of the string representing the year

        :param matchobj: the result of :py:meth:`re.sub`
        :return: the last two digits of the string representing the year
        """
        return matchobj.group(0)[2:]

    def _init_date(self):
        """Create a properly formatted string containing the date of the event"""
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
    def _parse_prerequisites(personal, material, financial, offers):
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

    def _build_description(self, link=""):
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

    @create_reduced_after_full
    def get_full_row(self, subtable_title=None):
        """Exchange a table row with all the event's information against a
        subtable's title

        This ensures, that after handing over the full information, the reduced
        version with a reference to the subtable containing the  full version is
        created.

        .. note:: This is ensured by a decorator, which is why the function
            signature on `ReadTheDocs.org
            <https://pyxml2pdf.readthedocs.io/en/latest/pyxml2pdf.html#Core.events
            .Event.get_full_row>`_ is displayed incorrectly. The parameter and
            return value are as follows...

        :param str subtable_title: the title of the subtable in which the row will
            be integrated
        :returns: a table row with all the event's information
        :rtype: Table
        """
        return self._full_row

    @property
    def categories(self):
        """Return the event's categories

        :returns: a list of the event's categories
        :rtype: List[str]
        """
        return self._categories

    @property
    def responsible(self):
        """Return the name of the person being responsible for the event

        :returns: first and last name
        :rtype: str
        """
        return self._responsible

    @property
    def date(self):
        """Return the date of the event

        :returns: date
        :rtype: str
        """
        return self._date

    def get_table_row(self, subtable_title):
        """Return the table row representation of the event

        This is the API of :py:class:`Core.events.Event` for getting the table row
        representation of the event. It makes sure, that on the first call
        :meth:`get_full_row` is invoked and otherwise :attr:`_reduced_row` is returned.

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
