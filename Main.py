from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from lxml import etree
from Parser import *
import sys
from colorama import Fore, Back, Style

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def validation():
    if len(sys.argv) < 4:
        raise Exception("Not enough arguments")
    if ".xml" not in sys.argv[1]:
        raise Exception("No XML file detected")
    if ".pdf" not in sys.argv[2]:
        raise Exception("File must have PDF extension")
    if ".properties" not in sys.argv[3]:
        raise Exception("Properties file must have .properties extension")


if __name__ == "__main__":
    pdfmetrics.registerFont(TTFont('Theano-Modern', 'TheanoModern-Regular.ttf'))
    data = []
    validation()
    parser = PDFBuilder(data, sys.argv[3])
    pdf = SimpleDocTemplate(sys.argv[2], pagesize=letter)
    doc = etree.parse(sys.argv[1])

    task_groups = doc.findall("taskGroup")
    title = doc.find("title")
    object_data = doc.find("object.data")

    parser.parse_xml_data(title, object_data, task_groups)

    pdf.build(data)
    print("\n" + Fore.GREEN + Back.BLUE + Style.BRIGHT +
          "--------------------------------------DONE--------------------------------------")
