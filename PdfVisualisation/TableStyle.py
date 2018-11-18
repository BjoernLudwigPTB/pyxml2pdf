from PdfVisualisation.Styles import *


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

    def modify_heading(self, new_style):
        self.heading = new_style

    def modify_sub_heading(self, new_style):
        self.sub_heading = new_style

    def modify_normal_style(self, new_style):
        self.normal = new_style
