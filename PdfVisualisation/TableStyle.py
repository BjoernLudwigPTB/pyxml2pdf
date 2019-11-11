from reportlab.lib import colors
from reportlab.lib.pagesizes import mm

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
            14.2 * mm,
            18.7 * mm,
            13.9 * mm,
            1 * mm,
            18 * mm,
            47 * mm,
        ]
        self._column_widths[4] = (
            self.table_width
            - sum(self._column_widths[0:4])
            - sum(self._column_widths[5:7])
        )

    def get_column_widths(self):
        return self._column_widths
