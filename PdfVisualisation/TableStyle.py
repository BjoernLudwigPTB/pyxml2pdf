import os
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

from PdfVisualisation.Styles import Styles


class TableStyle:
    """ Create a collection of styling information about the table to create

    Beautiful colors are:
        *   aliceblue (nicht mit azure)
        *   azure (nicht mit aliceblue)
        *   honeydew
        * ...
    """

    def __init__(self):
        self.heading = [
            Styles.valign_middle,
            Styles.background(colors.honeydew),
            Styles.box(colors.black),
            Styles.inner_grid(colors.black),
            Styles.align_center,
        ]

        self.sub_heading = [
            Styles.align_left,
            Styles.valign_middle,
            Styles.box(colors.black),
            Styles.inner_grid(colors.black),
            Styles.leftpadding_reduce,
            Styles.rightpadding_reduce,
        ]

        self.normal = [
            Styles.align_left,
            Styles.valign_middle,
            Styles.box(colors.black),
            Styles.inner_grid(colors.black),
            Styles.leftpadding_reduce,
            Styles.rightpadding_reduce,
        ]

        self.table_width = 177.8 * mm

        self._column_widths = [
            7.2 * mm,
            11.5 * mm,
            18.7 * mm,
            14.5 * mm,
            1 * mm,
            18 * mm,
            47 * mm,
        ]
        self._column_widths[4] = (
            self.table_width
            - sum(self._column_widths[0:4])
            - sum(self._column_widths[5:7])
        )

        # Set the resulting tables' styling with all the customization of
        # margins, fonts, fontsizes, etc...

        # Get custom_styles for all headings, texts, etc. from sample
        custom_styles = getSampleStyleSheet()
        # Overwrite the sample styles according to our needs.
        # TODO this should be provided in the properties file
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
        self._custom_styles = custom_styles

        # Register font with reportlab.
        self._init_font_family()

    @staticmethod
    def _init_font_family():
        """Register the desired font with :py:mod:`reportlab`

        This ensures that `<i></i>` and `<b></b>` as cell content work well.

        TODO this is much to hard coded and needs some serious refactoring
        """
        # Sadly we did not manage to properly configure readthedocs to load the
        # fonts on import from the paths everybody else uses, so we need to
        # manipulate them.
        path_to_fonts = "PdfVisualisation/"
        if not os.path.exists(path_to_fonts):
            path_to_fonts = "../" + path_to_fonts

        # Finally lead and register fonts with reportlab.
        registerFont(
            TTFont("NewsGothBT", Path(path_to_fonts + "NewsGothicBT-Roman.ttf"))
        )
        registerFont(
            TTFont("NewsGothBT_Bold", Path(path_to_fonts + "NewsGothicBT-Bold.ttf"))
        )
        registerFont(
            TTFont("NewsGothBT_Italic", Path(path_to_fonts + "NewsGothicBT-Italic.ttf"))
        )
        registerFont(
            TTFont(
                "NewsGothBT_BoldItalic",
                Path(path_to_fonts + "NewsGothicBT-BoldItalic.ttf"),
            )
        )
        registerFontFamily(
            "NewsGothBT",
            normal="NewsGothBT",
            bold="NewsGothBT_Bold",
            italic="NewsGothBT_Italic",
            boldItalic="NewsGothBT_BoldItalic",
        )

    @property
    def column_widths(self):
        """Return the column widths for the tables

        :returns List[float]: the list of column widths
        """
        return self._column_widths

    @property
    def custom_styles(self):
        """Return the custom stylesheet for the tables

        :returns reportlab.lib.styles.StyleSheet1: the custom stylesheet
        """
        return self._custom_styles
