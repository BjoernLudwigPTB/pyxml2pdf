from typing import List
from xml.etree.ElementTree import Element

from reportlab.platypus import Table
from reportlab.platypus import Paragraph

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator


class Item(Element):

    _categories: List[str]
    _item: Table
    _element: Element

    def __init__(self, element):
        self._element = element
        self._creator = Creator()
        self._styles = TableStyle.get_custom_styles()
        table_style = TableStyle()
        self._column_widths = table_style.get_column_widths()
        self._normal_style = table_style.normal
        self._init_categories()

    def _init_categories(self):
        """
        Initialize the list of categories from the content of the "Kategorie" tag
        gathered from the xml.

        :returns: `True` if the categories were successfully extracted
        :rtype: int
        """
        categories: str = self._concatenate_tags_content(["Kategorie"])
        self._categories = categories.split(", ")
        return 1

    def _concatenate_tags_content(self, item_tags, separator=" - "):
        """ Form one string from the content of a list of an item's XML tags

        Form a string of the content for all desired item tags by concatenating them
        together with a separator. This is especially necessary, since
        :py:mod:`reportlab.platypus.Paragraph` cannot handle `None`s as texts but
        handles as well the concatenation of XML tags' content, if `item_tags` has more
        than one element.

        :param List[str] item_tags: list of all tags for which the
            descriptive texts is wanted, even if it is just one
        :param str separator: the separator in between the concatenated texts
        :returns str: concatenated, separated texts of all tags for the current item
        """
        item_data_string: str = ""
        for tag in item_tags:
            data_string: str = self._element.findtext(tag)
            if data_string:
                if item_data_string:
                    item_data_string += separator + data_string
                else:
                    item_data_string = data_string
        return item_data_string

    def collect_item_content(self):
        """
        Extract interesting information from item and append them to result of a a
        nicely formatted row of a table.

        :returns Table: single row table containing all relevant item data
        """
        columns_to_print = [
            Paragraph(
                self._concatenate_tags_content(["Kursart"]), self._styles["Normal"]
            ),
            Paragraph(
                self._parse_date(
                    self._concatenate_tags_content(
                        ["TerminDatumVon1", "TerminDatumBis1"]
                    )
                ),
                self._styles["Normal"],
            ),
            Paragraph(self._concatenate_tags_content(["Ort1"]), self._styles["Normal"]),
            Paragraph(
                self._concatenate_tags_content(["Kursleiter"]), self._styles["Normal"]
            ),
            Paragraph(
                self._init_description(
                    self._concatenate_tags_content(["Bezeichnung"]),
                    self._concatenate_tags_content(["Bezeichnung2"]),
                    self._concatenate_tags_content(["Beschreibung"]),
                    self._concatenate_tags_content(["TrainerURL"]),
                ),
                self._styles["Normal"],
            ),
            Paragraph(
                self._concatenate_tags_content(["Zielgruppe"]), self._styles["Normal"]
            ),
            Paragraph(
                self._parse_prerequisites(
                    self._concatenate_tags_content(["Voraussetzung"]),
                    self._concatenate_tags_content(["Ausruestung"]),
                    self._concatenate_tags_content(["Kurskosten"]),
                    self._concatenate_tags_content(["Leistungen"]),
                ),
                self._styles["Normal"],
            ),
        ]
        self._item = self._creator.create_fixedwidth_table(
            [columns_to_print], self._column_widths, self._normal_style
        )
        return 1

    @staticmethod
    def _parse_date(date):
        """
        Determine the correct date for printing.

        :param str date: xml tag for relevant date.
        :returns: the text to insert in date column of the current item
        :rtype: str
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
        the current item
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

        :param str name: the short name for the item
        :param str name2: the short name number two for the item
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
        """Return the item's categories.

        :return List[str]: a list of the item's categories
        """
        return self._categories
