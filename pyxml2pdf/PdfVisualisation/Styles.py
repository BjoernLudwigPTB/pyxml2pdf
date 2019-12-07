class Styles:

    align_center = ("ALIGN", (0, 0), (-1, -1), "CENTER")
    valign_middle = ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    valign_top = ("VALIGN", (0, 0), (-1, -1), "TOP")
    align_left = ("ALIGN", (0, 0), (-1, -1), "LEFT")
    leftpadding_reduce = ("LEFTPADDING", (0, 0), (-1, -1), 3)
    rightpadding_reduce = ("RIGHTPADDING", (0, 0), (-1, -1), 2)

    @staticmethod
    def inner_grid(colors):
        return "INNERGRID", (0, 0), (-1, -1), 0.25, colors

    @staticmethod
    def box(colors):
        return "BOX", (0, 0), (-1, -1), 0.25, colors

    @staticmethod
    def background(colors):
        return "BACKGROUND", (0, 0), (-1, -1), colors

    @staticmethod
    def font_size(size):
        return "FONTSIZE", (0, 0), (-1, -1), size
