from reportlab.platypus import Table


class Creator:
    @staticmethod
    def create_table_fixed(elements, widths, style):
        t = Table(elements, colWidths=widths)
        t.setStyle(style)

        return t
