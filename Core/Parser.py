from typing import List

import reportlab
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

from PdfVisualisation.TableStyle import TableStyle
from model.tables.Creator import Creator
from model.tables.TableBuilder import TableBuilder


class PDFBuilder:
    _elements: List[reportlab.platypus.Table]

    def __init__(self, elements, properties):
        self._elements = elements
        self._creator = Creator()
        self._table_styles = TableStyle()
        PDFBuilder._set_font_family()
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
        custom_styles.get("Normal").fontSize = 7
        custom_styles.get("Normal").leading = custom_styles[
                                                  "Normal"].fontSize * 1.2
        custom_styles.get("Normal").fontName = 'NewsGothBT'
        custom_styles.get("Italic").fontSize = custom_styles[
            "Normal"].fontSize
        custom_styles.get("Italic").leading = custom_styles[
                                                  "Italic"].fontSize * 1.2
        custom_styles.get("Italic").fontName = 'NewsGothBT_Italic'
        custom_styles.get("Heading1").fontSize = 12
        custom_styles.get("Heading1").leading = custom_styles[
                                                    "Heading1"].fontSize * 1.2
        custom_styles.get("Heading1").fontName = 'NewsGothBT_Bold'
        custom_styles.get("Heading2").fontSize = custom_styles[
            "Normal"].fontSize
        custom_styles.get("Heading2").leading = custom_styles[
                                                    "Heading2"].fontSize * 1.2
        custom_styles.get("Heading2").fontName = 'NewsGothBT_Bold'
        return custom_styles

    @staticmethod
    def _set_font_family():
        """
        Register the desired font with `reportlab` to make sure that
        `<i></i>` and `<b></b>` work well.
        """
        registerFont(TTFont('NewsGothBT',
                            'PdfVisualisation/NewsGothicBT-Roman.ttf'))
        registerFont(TTFont('NewsGothBT_Bold',
                            'PdfVisualisation/NewsGothicBT-Bold.ttf'))
        registerFont(TTFont('NewsGothBT_Italic',
                            'PdfVisualisation/NewsGothicBT-Italic.ttf'))
        registerFont(TTFont('NewsGothBT_BoldItalic',
                            'PdfVisualisation/NewsGothicBT-BoldItalic.ttf'))
        registerFontFamily(
            'NewsGothBT', normal='NewsGothBT', bold='NewsGothBT_Bold',
            italic='NewsGothBT_Italic',
            boldItalic='NewsGothBT_BoldItalic')

    @staticmethod
    def _get_event_data(event_data, event_data_tags):
        """
        Form a string of the descriptive texts for all desired event tags
        by concatenating them with a separator. This is especially necessary,
        since `reportlab.platypus.Paragraph` cannot handle `None`s as texts.

        :param xml.etree.ElementTree.Element event_data: the event from where
            the texts shall be extracted
        :param List[str] event_data_tags: list of all tags for which the
            descriptive texts is wanted, even if it is just one
        :return str: the texts of all tags under the current event
        """
        event_data_string = ""
        for tag in event_data_tags:
            data_string = event_data.findtext(tag)
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
            personal_string = 'a) ' + personal + '<br/>'
        else:
            personal_string = 'a) keine <br/>'

        if material:
            material_string = 'b) ' + material + '<br/>'
        else:
            material_string = 'b) keine <br/>'

        if financial:
            financial_string = 'c) ' + financial + ' € (' + offers + ')'
        else:
            financial_string = 'c) keine'
        return personal_string + material_string + financial_string

    @staticmethod
    def _parse_date(date):
        """
        Determine the correct date for printing.

        TODO implement filtering of emtpy dates and '00:00'

        :param str date: xml tag for relevant date.
        :return str: the text to insert in date column of the current event
        """
        if date:
            date_string = date
        else:
            date_string = ""
        return date_string

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
                categories = PDFBuilder.get_event_categories(
                    event, PDFBuilder._get_event_data(event, ['Kategorie']))
                self._table_manager.distribute_events(
                    self.collect_event_data(event), categories)
            subtable_elements = self._table_manager.collect_subtables()
            for subtable_element in subtable_elements:
                self._elements.append(subtable_element)
            return self.get_elements()
        else:
            print("No events list found.")

    def collect_event_data(self, event_data):
        """
        Extract interesting information from event and append them to print
        out data in `_elements`.

        :param xml.etree.ElementTree.Element event_data: the event from
            which the texts shall be extracted into a nicely formatted row of a
            table to insert in print out `_elements`
        :return reportlab.platypus.Table: single row table containing all
            relevant event data
        """
        if event_data is not None:
            styles = self._styles
            columns_to_print = [
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Kursart']), styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['TerminDatumVon1', 'TerminDatumBis1']),
                    styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Ort1']), styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Kursleiter']), styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Bezeichnung', 'Bezeichnung2',
                                 'Beschreibung']), styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Zielgruppe']), styles["Normal"]),
                Paragraph(PDFBuilder._parse_prerequisites(
                    PDFBuilder._get_event_data(
                        event_data, ['Voraussetzung']),
                    PDFBuilder._get_event_data(event_data, ['Ausrüstung']),
                    PDFBuilder._get_event_data(event_data, ['Kurskosten']),
                    PDFBuilder._get_event_data(event_data, ['Leistungen'])),
                    styles["Normal"]),
                Paragraph(PDFBuilder._get_event_data(
                    event_data, ['Bemerkungen']), styles["Normal"])]
            event = self._creator.create_table_fixed(
                [columns_to_print], self._table_styles.column_widths,
                self._table_styles.normal)
            return event
        else:
            print("No events found.")

    def get_elements(self):
        """
        Return the collected event table.

        :return List[reportlab.platypus.Table]: a list of all table rows
            containing the relevant event data
        """
        return self._elements

    @staticmethod
    def get_event_categories(event, category_text):
        """
        Construct a list of categories from the string gathered out of the xml.

        :param defusedxml.ElementTree.Element event: event for which the
            categories are needed
        :param category_text: the text from the xml file containing the
            activities covered by the event
        :return List[str]: the list of the categories
        """
        categories = PDFBuilder._get_event_data(event, ['Kategorie'])
        return categories.split(', ')
