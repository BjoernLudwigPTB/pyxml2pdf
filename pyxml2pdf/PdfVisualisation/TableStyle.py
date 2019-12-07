from pathlib import PurePath

from reportlab.lib import colors
from reportlab.lib.pagesizes import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont

from pyxml2pdf.PdfVisualisation.Styles import Styles


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

        # This specifies the column widths of the final result. The columns contain...
        self._column_widths = [
            # ... the type of the event.
            7.2 * mm,
            # ... the date and time of the event.
            11.5 * mm,
            # ... the region of the event.
            18.7 * mm,
            # ... the responsible person for the event.
            14.5 * mm,
            # ... the details regarding the content of the event. Note that this
            # column width is calculated in the next step from the available total
            # space and the sum of all other column widths.
            0 * mm,
            # ... the target audience the event.
            18 * mm,
            # ... the personal, material and financial prerequisites for the event.
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
        """
        # Set root of fonts to the folder containing this file.
        path_to_fonts = PurePath(__file__).parent

        # Finally lead and register fonts with reportlab.
        registerFont(
            TTFont("NewsGothBT", path_to_fonts.joinpath("NewsGothicBT-Roman.ttf"))
        )
        registerFont(
            TTFont("NewsGothBT_Bold", path_to_fonts.joinpath("NewsGothicBT-Bold.ttf"))
        )
        registerFont(
            TTFont(
                "NewsGothBT_Italic", path_to_fonts.joinpath("NewsGothicBT-Italic.ttf")
            )
        )
        registerFont(
            TTFont(
                "NewsGothBT_BoldItalic",
                path_to_fonts.joinpath("NewsGothicBT-BoldItalic.ttf"),
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

        :returns: the list of column widths
        :rtype: List[float]
        """
        return self._column_widths

    @property
    def custom_styles(self):
        """Return the custom stylesheet for the tables

        :returns: the custom stylesheet
        :rtype: reportlab.lib.styles.StyleSheet1
        """
        return self._custom_styles
