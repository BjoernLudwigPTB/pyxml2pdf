from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from lxml import etree
from Parser import *

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


if __name__ == "__main__":
    pdfmetrics.registerFont(TTFont('Theano-Modern', 'TheanoModern-Regular.ttf'))
    data = []
    parser = PDFBuilder(data, "input/template_prop.properties")
    pdf = SimpleDocTemplate("mypdf.pdf", pagesize=letter)
    doc = etree.parse("input/template.xml")

    task_groups = doc.findall("taskGroup")
    title = doc.find("title")
    object_data = doc.find("object.data")

    parser.parse_xml_data(title, object_data, task_groups)

    pdf.build(data)
    print("\n" + "--------------------------------------DONE--------------------------------------")
