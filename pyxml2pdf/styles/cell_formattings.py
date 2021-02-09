class CellFormattingCommands:
    """This class contains some cell formatting commands explained from
    page 85 on in the `reportlab user guide <https://www.reportlab.com/docs/reportlab-
    userguide.pdf>`_.

    A command is structured as a tuple containing a descriptive string representing
    the command class, the first and the last cell on which the command should be
    invoked and the parameter value for the command. For details see the link.
    """

    align_center = ("ALIGN", (0, 0), (-1, -1), "CENTER")
    valign_middle = ("VALIGN", (0, 0), (-1, -1), "MIDDLE")
    valign_top = ("VALIGN", (0, 0), (-1, -1), "TOP")
    align_left = ("ALIGN", (0, 0), (-1, -1), "LEFT")
    leftpadding_reduce = ("LEFTPADDING", (0, 0), (-1, -1), 3)
    rightpadding_reduce = ("RIGHTPADDING", (0, 0), (-1, -1), 3)

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
