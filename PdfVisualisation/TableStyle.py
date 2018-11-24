from reportlab.lib import colors
from reportlab.lib.pagesizes import mm

from PdfVisualisation.Styles import Styles


class TableStyle:
    def __init__(self):
        self.heading = [
            Styles.align_left, Styles.valign_middle,
            Styles.background(colors.lightgrey), Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.sub_heading = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.normal = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.columm_widths = [8 * mm, 18 * mm, 20 * mm, 18 * mm, 40 * mm,
                              21 * mm, 27 * mm, 26 * mm]

        self.table_width = 178 * mm
