from reportlab.lib.pagesizes import inch
from reportlab.platypus import Paragraph, Table

from PdfVisualisation.FlowableRect import FlowableRect


class Creator:
    @staticmethod
    def create_table(elements, width, style):

        row = 0
        for elem in elements:
            if elem.__len__() > row:
                row = elem.__len__()

        t = Table(elements, row * [width * inch])
        t.setStyle(style)

        return t

    @staticmethod
    def create_table_fixed(elements, widths, style):
        t = Table(elements, colWidths=widths)
        t.setStyle(style)

        return t

    @staticmethod
    def make_checkbox_form(task, desc, styles):
        desc[0].append(Paragraph("Yes", styles))
        desc[0].append(FlowableRect(5, 5, True if task == "true" else False))
        desc[0].append(Paragraph("No", styles))
        desc[0].append(FlowableRect(5, 5, False if task == "true" else True))
