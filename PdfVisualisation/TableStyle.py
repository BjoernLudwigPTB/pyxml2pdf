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
            Styles.inner_grid(colors.black)]

        self.normal = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.column_widths = [8 * mm, 13 * mm, 19 * mm, 18 * mm, 65 * mm,
                              20 * mm, 35 * mm]
        # [8 * mm, 13 * mm, 19 * mm, 18 * mm, 50 * mm, 20 * mm, 30 * mm,
        # 20 * mm]

        self.table_width = 178 * mm
