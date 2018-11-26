from reportlab.lib import colors
from reportlab.lib.pagesizes import mm

from PdfVisualisation.Styles import Styles


class TableStyle:
    def __init__(self):
        """
        schöne Farben sind:
            *   aliceblue (nicht mit azure)
            *   azure (nicht mit aliceblue)
            * ...
        """
        self.heading = [
            Styles.valign_middle, Styles.background(colors.honeydew),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.sub_heading = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black), Styles.leftpadding_reduce,
            Styles.rightpadding_reduce]

        self.normal = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black), Styles.leftpadding_reduce,
            Styles.rightpadding_reduce]

        self.table_width = 178 * mm

    def get_column_widths(self):
        column_widths = [8 * mm, 13 * mm, 19 * mm, 15 * mm, 1 * mm,
                         18 * mm, 47 * mm]
        column_widths[4] = self.table_width - sum(
            column_widths[0:4]) - sum(column_widths[5:7])
        return column_widths
