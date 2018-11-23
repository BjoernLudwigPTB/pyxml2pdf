from defusedxml.ElementTree import parse
from reportlab.lib.pagesizes import landscape, A5
from reportlab.platypus import SimpleDocTemplate

from Core.Parser import PDFBuilder


class Initializer:
    def __init__(self):
        self.__data = []

    def build(self, input_t, output_t, properties_t):
        """
        Coordinate the construction of the pdf result.

        Parameters
        ----------
            :type input_t: str := path to input xml-file
            :type output_t:str := path to pdf file containing result
            :type properties_t:str := path to text file containing properties
        """

        parser = PDFBuilder(self.__data, properties_t)
        pdf = SimpleDocTemplate(output_t, pagesize=landscape(A5))
        doc = parse(input_t)

        courses = doc.findall("kurs")

        parser.parse_xml_data(courses)

        pdf.build(self.__data)
