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
        self.heading1 = [
            Styles.valign_middle, Styles.background(colors.honeydew),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading2 = [
            Styles.valign_middle, Styles.background(colors.chartreuse),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading3 = [
            Styles.valign_middle, Styles.background(colors.fuchsia),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading4 = [
            Styles.valign_middle, Styles.background(colors.blueviolet),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading5 = [
            Styles.valign_middle, Styles.background(colors.blanchedalmond),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading6 = [
            Styles.valign_middle, Styles.background(colors.bisque),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading7 = [
            Styles.valign_middle, Styles.background(colors.azure),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.heading8 = [
            Styles.valign_middle, Styles.background(colors.beige),
            Styles.box(colors.black), Styles.inner_grid(colors.black),
            Styles.align_center]

        self.sub_heading = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.normal = [
            Styles.align_left, Styles.valign_middle, Styles.box(colors.black),
            Styles.inner_grid(colors.black)]

        self.heading_iterator = iter([self.heading1, self.heading5,
                                     self.heading2, self.heading6,
                                     self.heading3, self.heading7,
                                     self.heading4, self.heading8])

        self.color_list = [Styles.background(colors.beige),
                           Styles.background(colors.azure),
                           Styles.background(colors.bisque),
                           Styles.background(colors.blanchedalmond),
                           Styles.background(colors.blueviolet),
                           Styles.background(colors.chartreuse),
                           Styles.background(colors.crimson),
                           Styles.background(colors.floralwhite),
                           Styles.background(colors.forestgreen),
                           Styles.background(colors.fuchsia),
                           Styles.background(colors.goldenrod),
                           Styles.background(colors.honeydew)]

        self.color_iterator = iter(self.color_list)

        self.column_widths = [8 * mm, 13 * mm, 19 * mm, 18 * mm, 46 * mm,
                              21 * mm, 30 * mm, 23 * mm]

        self.table_width = 178 * mm
