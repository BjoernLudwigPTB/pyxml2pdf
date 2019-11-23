from typing import List
from xml.etree.ElementTree import Element

from reportlab.platypus import Paragraph
from reportlab.platypus import Table

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator


class Event(Element):
    """*Event* is a wrapper class for :py:mod:`xml.etree.ElementTree.Element`

    :py:mod:`xml.etree.ElementTree.Element` is augmented with the table row
    representation and the attributes and methods to manipulate everything
    according to the final tables needs. An :py:mod:`Core.events.Event` can only
    be initialized with an object of type
    :py:mod:`xml.etree.ElementTree.Element`.

    :param xml.etree.ElementTree.Element element: the element on which *event*
        should be based
    """

    _categories: List[str]
    _full_row: Table
    _reduced_row: Table
    _subtable_title: str

    def __init__(self, element):
        # Call Element constructor and extend ourselves by extending all children
        # tags to create an underlying copy of element.
        super().__init__(element.tag, element.attrib)
        self.extend(list(element))
        # Initialize needed objects especially for table creation.
        self._creator = Creator()
        table_style = TableStyle()
        self._style = table_style.get_custom_styles()["Normal"]
        self._column_widths = table_style.get_column_widths()
        self._normal_style = table_style.normal
        # Initialize definitely needed instance variables.
        self._init_categories()
        self._init_full_row()

    def _init_categories(self):
        """
        Initialize the list of categories from the content of the "Kategorie" tag
        gathered from the xml.

        :returns int: `True` if the categories were successfully extracted
        """
        categories: str = self._concatenate_tags_content(["Kategorie"])
        self._categories = categories.split(", ")
        return 1

    def _init_reduced_row(self, subtable_title):
        """Initializes the reduced version of the event

        Create a table row in proper format but just containing a brief description
        of the event and a reference to the fully described event at another place,
        namely the subtable with the given title.

        :param str subtable_title: title of the subtable which contains the full event
        """
        self._reduced_row = Table([subtable_title])

    def create_reduced_after_full(f):
        def decorate(*args, **kwargs):
            ret = f(*args, **kwargs)
            args[0]._init_reduced_row(args[1])
            return ret

        return decorate

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
        :returns str: concatenated, separated texts of all tags for the current event
        """
        children_text = ""  # type: str
        for tag in event_subelements:
            child_text: str = self.findtext(tag)
            if child_text:
                if children_text:
                    children_text += separator + child_text
                else:
                    children_text = child_text
        return children_text

    def _init_full_row(self):
        """Initialize the single table row containing all information of the event

        Extract interesting information from events children tags and connect them
        into a nicely formatted row of a table.
        """
        columns_to_print = [
            Paragraph(self._concatenate_tags_content(["Kursart"]), self._style),
            Paragraph(
                self._parse_date(
                    self._concatenate_tags_content(
                        ["TerminDatumVon1", "TerminDatumBis1"]
                    )
                ),
                self._style,
            ),
            Paragraph(self._concatenate_tags_content(["Ort1"]), self._style),
            Paragraph(self._concatenate_tags_content(["Kursleiter"]), self._style),
            Paragraph(
                self._init_description(
                    self._concatenate_tags_content(["Bezeichnung"]),
                    self._concatenate_tags_content(["Bezeichnung2"]),
                    self._concatenate_tags_content(["Beschreibung"]),
                    self._concatenate_tags_content(["TrainerURL"]),
                ),
                self._style,
            ),
            Paragraph(self._concatenate_tags_content(["Zielgruppe"]), self._style),
            Paragraph(
                self._parse_prerequisites(
                    self._concatenate_tags_content(["Voraussetzung"]),
                    self._concatenate_tags_content(["Ausruestung"]),
                    self._concatenate_tags_content(["Kurskosten"]),
                    self._concatenate_tags_content(["Leistungen"]),
                ),
                self._style,
            ),
        ]
        self._full_row = self._creator.create_fixedwidth_table(
            [columns_to_print], self._column_widths, self._normal_style
        )

    @staticmethod
    def _parse_date(date):
        """
        Determine the correct date for printing.

        :param str date: xml tag for relevant date.
        :returns str: the text to insert in date column of the current event
        """
        if "2099" in date:
            date_string = "auf Anfrage"
        elif date:
            date_string = (
                date.replace("00:00", "")
                .replace("2020", "20")
                .replace("2019", "19")
                .replace("2018", "18")
            )
        else:
            date_string = ""
        return date_string

    @staticmethod
    def _parse_prerequisites(personal, material, financial, offers):
        """
        Determine all prerequisites and assemble a string accordingly.

        :param str material: material prerequisite xml text
        :param str personal: personal prerequisite xml text
        :param str financial: financial prerequisite xml text
        :param str offers: xml text of what is included in the price
        :returns str: the text to insert in prerequisite column
            the current event
        """
        if personal:
            personal_string = "a) " + personal + "<br/>"
        else:
            personal_string = "a) keine <br/>"

        if material:
            material_string = "b) " + material + "<br/>"
        else:
            material_string = "b) keine <br/>"

        if financial:
            financial_string = "c) " + financial + " € (" + offers + ")"
        else:
            financial_string = "c) keine"
        return personal_string + material_string + financial_string

    def _init_description(self, name, name2, description, url):
        """
        Concatenate the description and the url if provided.

        :param str name: the short name for the event
        :param str name2: the short name number two for the event
        :param str description: the descriptive text
        :param str url: the trainer's homepage url
        :returns str: the full description including url if provided
        """
        if name:
            full_description = "<b>" + name + "</b>"
        else:
            full_description = ""

        if name2:
            full_description += " - " + name2

        if description:
            full_description += " - " + description

        if url:
            full_description += " Mehr Infos unter: " + url + "."

        self._full_description = full_description

        return full_description

    def get_categories(self):
        """Return the event's categories

        :returns List[str]: a list of the event's categories
        """
        return self._categories

    @create_reduced_after_full
    def get_full_row(self, subtable_title=None):
        """Exchange a table row with all the event's information with a subtable's title

        This ensures, that after handing over the full information, the reduced
        version with a reference to the subtable containing the  full version is
        created.
        :returns Table: a table row with all the event's information
        """
        # If subtable_title is provided, we assume the event has been written to this
        # according subtable, so we store, that the event can be found there.
        if subtable_title:
            self._subtable_title = subtable_title
        else:
            try:
                self._subtable_title
            except AttributeError:
                raise RuntimeError(
                    "No title for a reference to the full event was given by any "
                    "previous call. Thus it needs to be given this time."
                )
        return self._full_row

    def get_reduced_row(self):
        """Return a table row with a reference to where to find the full information

        :returns Table: a table row with some of the event's information
        """
        return self._reduced_row
