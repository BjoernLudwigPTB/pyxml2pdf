from reportlab.platypus import Table


class Creator:
    @staticmethod
    def create_fixedwidth_table(elements, widths, style):
        """ Create and return a table with specified column widths

        Create a table from specified elements with fixed column widths and a specific
        style.

        :param  elements: the elements to include in the table
        :param widths: the column widths
        :param style: the style in which the table shall appear
        :returns: table containing all specified elements in fixed width columns
        :rtype: Table
        """
        t = Table(elements, colWidths=widths)
        t.setStyle(style)

        return t
