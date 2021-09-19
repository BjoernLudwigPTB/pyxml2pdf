"""This module contains the class :class:`Initializer` to coordinate the process."""

from typing import List

from defusedxml.ElementTree import parse  # type: ignore
from reportlab.lib.units import mm  # type: ignore
from reportlab.platypus import SimpleDocTemplate  # type: ignore
from reportlab.platypus.flowables import KeepTogether  # type: ignore

from pyxml2pdf.core.parser import Parser
from pyxml2pdf.core.post_processor import PostProcessor
from pyxml2pdf.core.sorter import Sorter
from pyxml2pdf.input.properties import (
    pagesize,
    rows_xmltag,
    sort_xmltag,
)  # type: ignore


class Initializer:
    """Coordinate the construction of the pdf result

    Keep strings together, start the actual parsing and build the PDF

    :param str input_path: Path to input XML file
    :param str output_path: Path to resulting PDF file
    """

    def __init__(self, input_path: str, output_path: str):
        #: The processed content of the XML file as table rows and columns
        self._data = []  # type: List[KeepTogether]
        parser = Parser(self._data)
        pdf = SimpleDocTemplate(
            output_path,
            pagesize=[size * mm for size in pagesize],
            topMargin=0.0,
            bottomMargin=0.0,
            leftMargin=0.0,
            rightMargin=0.0,
        )
        doc = parse(input_path)
        sorter = Sorter(doc.findall(rows_xmltag))
        sorted_courses = sorter.sort_parsed_xml(sort_xmltag)

        parser.collect_xml_data(sorted_courses)

        if self._data:
            pdf.build(self._data)

            pdf_postprocessor = PostProcessor(output_path)
            pdf_postprocessor.finalize_print_preparation()
