from lxml import etree
from reportlab.lib.pagesizes import landscape, A5
from reportlab.platypus import SimpleDocTemplate

from Core.Parser import PDFBuilder


class Initializer:
    def __init__(self):
        self.__data = []

    def build(self, input_t, output_t, properties_t, signature):
        parser = PDFBuilder(self.__data, properties_t)
        pdf = SimpleDocTemplate(output_t, pagesize=landscape(A5))
        doc = etree.parse(input_t)

        task_groups = doc.findall("taskGroup")
        title = doc.find("title")
        object_data = doc.find("object.data")

        parser.parse_xml_data(title, object_data, task_groups, signature)

        pdf.build(self.__data)
