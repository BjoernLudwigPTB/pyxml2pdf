from typing import List

from defusedxml.ElementTree import parse
from reportlab.lib.pagesizes import mm
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.flowables import KeepTogether

from Core.Parser import Parser
from Core.PostProcessor import PostProcessor
from Core.Sorter import Sorter


class Initializer:

    __data: List[KeepTogether]

    def __init__(self, input_path, output_path, properties_path):
        """
        Coordinate the construction of the pdf result.

        Parameters
        ----------
        :param str input_path: path to input xml-file
        :param str output_path: path to pdf file containing result
        :param str properties_path: path to text file containing properties
        """
        self.__data = []
        parser = Parser(properties_path, self.__data)
        pdf = SimpleDocTemplate(
            output_path,
            pagesize=(178 * mm, 134 * mm),
            topMargin=0.0,
            bottomMargin=0.0,
            leftMargin=0.0,
            rightMargin=0.0,
        )
        doc = parse(input_path)
        sorter = Sorter(doc.findall("kurs"))
        sorted_courses = sorter.sort_parsed_xml("TerminDatumVon1")

        parser.collect_xml_data(sorted_courses)

        pdf.build(self.__data)

        pdf_postprocessor = PostProcessor(output_path)
        pdf_postprocessor.finalize_print_preparation()
