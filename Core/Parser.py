import warnings
from typing import List

from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus.flowables import KeepTogether

from Core.events import Event
from model.tables.Creator import Creator
from model.tables.TableBuilder import TableBuilder


class Parser:

    _elements: List[KeepTogether]

    def __init__(self, properties, elements=[]):
        """
        XML parser to extract all interesting information from xml-data.

        :param str properties: path to the properties file
        :param List[KeepTogether] elements: optional elements to populate the Parser
        """
        self._elements = elements
        self._creator = Creator()
        Parser._set_font_family()
        self._table_manager = TableBuilder(properties)

    @staticmethod
    def _set_font_family():
        """
        Register the desired font with `reportlab` to make sure that
        `<i></i>` and `<b></b>` work well.

        TODO this is much to hard coded and needs some serious refactoring
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

    def collect_xml_data(self, events):
        """
        Traverse the parsed xml data and gather collected event data. Pass
        event data to table_manager and get collected data back.

        :param List[Event] events: a list of the items from which the texts shall be
            extracted into a nicely formatted row of a table to insert into result.
        :returns: list of all table rows containing the relevant event data
        :rtype: List[KeepTogether]
        """
        items = []
        if events is not None:
            for event in events:
                event = Event(event)
                categories = event.get_categories()
                self._table_manager.distribute_event(event)
            subtable_elements = self._table_manager.collect_subtables()
            for subtable_element in subtable_elements:
                self._elements.append(KeepTogether(subtable_element))
            return self._elements
        else:
            warnings.warn("There were no items to print.", RuntimeWarning)
