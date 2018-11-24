from reportlab.lib.pagesizes import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator
from PdfVisualisation.TableStyle import TableStyle
from model.tables.TableBuilder import TableBuilder


class PDFBuilder:
    def __init__(self, elements, properties):
        self._elements = elements
        self._creator = Creator()
        self._table_manager = TableBuilder(properties)
        self._table_style = TableStyle()
        PDFBuilder._set_font_family()

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
        Forms a string of the descriptive texts for all desired event tags
        by concatenating them seperated by ' + '. This is especially useful,
        since `reportlab.platypus.Paragraph` cannot handle `None`s as texts.

        :param xml.etree.ElementTree.Element event_data: the event from where
            the texts shall be extracted
        :param list(str) event_data_tags: list of all tags for which the
            descriptive texts is wanted
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

    def parse_xml_data(self, events):
        # Get styles for all headings, texts, etc. from sample
        styles = getSampleStyleSheet()
        styles.get("Normal").fontSize = 7
        styles.get("Normal").leading = styles["Normal"].fontSize * 1.2
        styles.get("Normal").fontName = 'NewsGothBT'
        styles.get("Italic").fontSize = styles["Normal"].fontSize
        styles.get("Italic").leading = styles["Italic"].fontSize * 1.2
        styles.get("Italic").fontName = 'NewsGothBT_Italic'
        styles.get("Heading1").fontSize = styles["Normal"].fontSize
        styles.get("Heading1").leading = styles["Heading1"].fontSize * 1.2
        styles.get("Heading1").fontName = 'NewsGothBT_Bold'
        self.parse_events(events, styles)

    def parse_event_data(self, event_data, styles):
        """
        Extract interesting information from event and append them to print
        out data in `_elements`.

        :param xml.etree.ElementTree.Element event_data: the texts shall be
            extracted
        :param reportlab.lib.styles.StyleSheet styles: a
        :return reportlab.platypus.Table: a nicely formatted row of a table to
            insert in print out `_elements`
        """
        if event_data is not None:
            columns = [
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
                [columns], [8*mm, 18*mm, 20*mm, 18*mm, 40*mm, 21*mm,
                            27*mm, 26*mm], self._table_style.normal)
            self._elements.append(event)
            return event
        else:
            print("No events found.")

    def parse_events(self, events, styles):
        if events is not None:
            for event in events:
                self.parse_event_data(event, styles)
        else:
            print("No events list found.")
