from reportlab.lib import colors
from reportlab.lib.pagesizes import mm
from reportlab.lib.styles import getSampleStyleSheet

from PdfVisualisation.Styles import Styles


class TableStyle:
    def __init__(self):
        """
        beautiful colors are:
            *   aliceblue (nicht mit azure)
            *   azure (nicht mit aliceblue)
            *   honeydew
            * ...
        """
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
        # Overwrite the sample styles according to our needs. TODO this should be provided in the properties file
        custom_styles.get("Normal").fontSize = 7
        custom_styles.get("Normal").leading = custom_styles[
                                                  "Normal"].fontSize * 1.2
        custom_styles.get("Normal").fontName = "NewsGothBT"
        custom_styles.get("Italic").fontSize = custom_styles["Normal"].fontSize
        custom_styles.get("Italic").leading = custom_styles[
                                                  "Italic"].fontSize * 1.2
        custom_styles.get("Italic").fontName = "NewsGothBT_Italic"
        custom_styles.get("Heading1").fontSize = 12
        custom_styles.get("Heading1").alignment = 1
        custom_styles.get("Heading1").leading = custom_styles[
                                                    "Heading1"].fontSize * 1.2
        custom_styles.get("Heading1").fontName = "NewsGothBT_Bold"
        custom_styles.get("Heading2").fontSize = custom_styles[
            "Normal"].fontSize
        custom_styles.get("Heading2").alignment = 1
        custom_styles.get("Heading2").leading = custom_styles[
                                                    "Heading2"].fontSize * 1.2
        custom_styles.get("Heading2").fontName = "NewsGothBT_Bold"
        self._custom_styles = custom_styles

    def get_column_widths(self):
        return self._column_widths
