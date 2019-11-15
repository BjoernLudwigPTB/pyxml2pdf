from typing import List

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import KeepTogether, Flowable, Paragraph

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator
from model.tables.TableBuilder import TableBuilder


class Parser:
    """XML parser to extract all interesting information"""

    _elements: List[Flowable]

    def __init__(self, elements, properties):
        self._elements = elements
        self._creator = Creator()
        self._table_styles = TableStyle()
        Parser._set_font_family()
        self._styles = self._style()
        self._table_manager = TableBuilder(properties, self._styles)

    @staticmethod
    def _style():
        """
        Do all the customization of styling regarding margins, fonts,
        fontsizes, etc..

        TODO make dependent on properties entries

        :return reportlab.lib.styles.StyleSheet: the created StyleSheet
        """
        # Get custom_styles for all headings, texts, etc. from sample
        custom_styles = getSampleStyleSheet()
        custom_styles.get("Normal").fontSize = 6.5
        custom_styles.get("Normal").leading = custom_styles["Normal"].fontSize * 1.2
        custom_styles.get("Normal").fontName = "NewsGothBT"
        custom_styles.get("Italic").fontSize = custom_styles["Normal"].fontSize
        custom_styles.get("Italic").leading = custom_styles["Italic"].fontSize * 1.2
        custom_styles.get("Italic").fontName = "NewsGothBT_Italic"
        custom_styles.get("Heading1").fontSize = 12
        custom_styles.get("Heading1").alignment = 1
        custom_styles.get("Heading1").leading = custom_styles["Heading1"].fontSize * 1.2
        custom_styles.get("Heading1").fontName = "NewsGothBT_Bold"
        custom_styles.get("Heading2").fontSize = custom_styles["Normal"].fontSize
        custom_styles.get("Heading2").alignment = 1
        custom_styles.get("Heading2").leading = custom_styles["Heading2"].fontSize * 1.2
        custom_styles.get("Heading2").fontName = "NewsGothBT_Bold"
        return custom_styles

    @staticmethod
    def _set_font_family():
        """
        Register the desired font with `reportlab` to make sure that
        `<i></i>` and `<b></b>` work well.
        """
        registerFont(TTFont("NewsGothBT", "PdfVisualisation/NewsGothicBT-Roman.ttf"))
        registerFont(
            TTFont("NewsGothBT_Bold", "PdfVisualisation/NewsGothicBT-Bold.ttf")
        )
        registerFont(
            TTFont("NewsGothBT_Italic", "PdfVisualisation/NewsGothicBT-Italic.ttf")
        )
        registerFont(
            TTFont(
                "NewsGothBT_BoldItalic", "PdfVisualisation/NewsGothicBT-BoldItalic.ttf"
            )
        )
        registerFontFamily(
            "NewsGothBT",
            normal="NewsGothBT",
            bold="NewsGothBT_Bold",
            italic="NewsGothBT_Italic",
            boldItalic="NewsGothBT_BoldItalic",
        )

    @staticmethod
    def _get_event_data(event, event_tags):
        """
        Form a string of the descriptive texts for all desired event tags
        by concatenating them with a separator. This is especially necessary,
        since `reportlab.platypus.Paragraph` cannot handle `None`s as texts.

        :param xml.etree.ElementTree.Element event: the event from where
            the texts shall be extracted
        :param List[str] event_tags: list of all tags for which the
            descriptive texts is wanted, even if it is just one
        :return str: the texts of all tags under the current event
        """
        event_data_string = ""
        for tag in event_tags:
            data_string = event.findtext(tag)
            if data_string:
                if event_data_string:
                    event_data_string += " - " + data_string
                else:
                    event_data_string = data_string
        return event_data_string

    @staticmethod
    def _parse_prerequisites(personal, material, financial, offers):
        """
        Determine all prerequisites and assemble a string accordingly.

        :param str material: material prerequisite xml text
        :param str personal: personal prerequisite xml text
        :param str financial: financial prerequisite xml text
        :param str offers: xml text of what is included in the price
        :return str: the text to insert in prerequisite column
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

    @staticmethod
    def _parse_date(date):
        """
        Determine the correct date for printing.

        :param str date: xml tag for relevant date.
        :return str: the text to insert in date column of the current event
        """
        if "2099" in date:
            date_string = "auf Anfrage"
        elif date:
            date_string = (
                date.replace("00:00", "").replace("2019", "19").replace("2018", "18")
            )
        else:
            date_string = ""
        return date_string

    @staticmethod
    def _parse_description(name, name2, description, url):
        """
        Concatenate the description and the url if provided.

        :param str name: the short name for the event
        :param str name: the short name number two for the event
        :param str description: the descriptive text
        :param str url: the trainer's homepage url
        :return str: the full description including url if provided
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

        return full_description

    def collect_xml_data(self, events):
        """
        Traverse the parsed xml data and gather collected event data. Pass
        event data to table_manager and get collected data back.

        :param List[defusedxml.ElementTree.Element] events: a list of the
            events from which the texts shall be extracted into a nicely
            formatted row of a table to insert in print out `_elements`
        :return List[reportlab.platypus.Table]: a list of all table rows
            containing the relevant event data
        """
        if events is not None:
            for event in events:
                categories = self.get_event_categories(event)
                self._table_manager.distribute_event(
                    self.collect_event_data(event), categories
                )
            subtable_elements = self._table_manager.collect_subtables()
            for subtable_element in subtable_elements:
                self._elements.append(KeepTogether(subtable_element))
            return self._elements
        else:
            print("No events list found.")

    def collect_event_data(self, event):
        """
        Extract interesting information from event and append them to print
        out data in `_elements`.

        :param xml.etree.ElementTree.Element event: the event from
            which the texts shall be extracted into a nicely formatted row of a
            table to insert in print out `_elements`
        :return reportlab.platypus.Table: single row table containing all
            relevant event data
        """
        if event is not None:
            styles = self._styles
            columns_to_print = [
                Paragraph(Parser._get_event_data(event, ["Kursart"]), styles["Normal"]),
                Paragraph(
                    Parser._parse_date(
                        self._get_event_data(
                            event, ["TerminDatumVon1", "TerminDatumBis1"]
                        )
                    ),
                    styles["Normal"],
                ),
                Paragraph(Parser._get_event_data(event, ["Ort1"]), styles["Normal"]),
                Paragraph(
                    Parser._get_event_data(event, ["Kursleiter"]), styles["Normal"]
                ),
                Paragraph(
                    Parser._parse_description(
                        Parser._get_event_data(event, ["Bezeichnung"]),
                        Parser._get_event_data(event, ["Bezeichnung2"]),
                        Parser._get_event_data(event, ["Beschreibung"]),
                        Parser._get_event_data(event, ["TrainerURL"]),
                    ),
                    styles["Normal"],
                ),
                Paragraph(
                    Parser._get_event_data(event, ["Zielgruppe"]), styles["Normal"]
                ),
                Paragraph(
                    Parser._parse_prerequisites(
                        Parser._get_event_data(event, ["Voraussetzung"]),
                        Parser._get_event_data(event, ["Ausruestung"]),
                        Parser._get_event_data(event, ["Kurskosten"]),
                        Parser._get_event_data(event, ["Leistungen"]),
                    ),
                    styles["Normal"],
                ),
            ]
            event = self._creator.create_table_fixed(
                [columns_to_print],
                self._table_styles.get_column_widths(),
                self._table_styles.normal,
            )
            return event
        else:
            print("No events found.")

    @staticmethod
    def get_event_categories(event):
        """
        Construct a list of categories from the string gathered out of the xml.

        :param defusedxml.ElementTree.Element event: event for which the
            categories are needed
        :return List[str]: the list of the categories
        """
        categories = Parser._get_event_data(event, ["Kategorie"])
        return categories.split(", ")
