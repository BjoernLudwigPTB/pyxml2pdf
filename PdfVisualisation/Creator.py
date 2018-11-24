from reportlab.lib.pagesizes import mm
from reportlab.platypus import Table


class Creator:
    @staticmethod
    def create_table(elements, width, style):
        """
        Is this maybe a table with equal column width? Does `row` contain the
        number of columns per row?

        TODO be clear about what the function does
        :param elements:
        :param width:
        :param style:
        :return:
        """
        row = 0
        for elem in elements:
            if elem.__len__() > row:
                row = elem.__len__()

        t = Table(elements, row * [width * mm])
        t.setStyle(style)

        return t

    @staticmethod
    def create_table_fixed(elements, widths, style):
        t = Table(elements, colWidths=widths)
        t.setStyle(style)

        return t
