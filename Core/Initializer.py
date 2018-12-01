from typing import List

import reportlab
from defusedxml.ElementTree import parse
from reportlab.lib.pagesizes import mm
from reportlab.platypus import SimpleDocTemplate

from Core.Parser import PDFBuilder
from Core.PostProcessor import PostProcessor
from Core.Sorter import Sorter


class Initializer:

    __data: List[reportlab.platypus.Table]

    def __init__(self):
        self.__data = []

    def build(self, input_t, output_t, properties_t):
        """
        Coordinate the construction of the pdf result.

        Parameters
        ----------
        :param str input_t: path to input xml-file
        :param str output_t: path to pdf file containing result
        :param str properties_t: path to text file containing properties
        """

        parser = PDFBuilder(self.__data, properties_t)
        pdf = SimpleDocTemplate(output_t, pagesize=(179 * mm, 134 * mm),
                                topMargin=0.0, bottomMargin=0.0,
                                leftMargin=0.0, rightMargin=0.0)
        doc = parse(input_t)
        courses = doc.findall('kurs')
        sorter = Sorter(doc, courses)
        sorted_courses = sorter.sort_parsed_xml('TerminDatumVon1')

        parser.collect_xml_data(sorted_courses)

        pdf.build(self.__data)

        processed_pdf = PostProcessor(output_t)
        processed_pdf.rotate(processed_pdf.get_path())
        processed_pdf.split()
