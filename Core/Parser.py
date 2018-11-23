import datetime
from enum import Enum

from reportlab.lib.enums import TA_RIGHT
from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.validators import isInstanceOf
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, Table

from PdfVisualisation.Creator import Creator
from PdfVisualisation.TableStyle import TableStyle
from model.tasks.TaskBuilder import TaskBuilder


class Signature(Enum):
    AUTO_DATE = 0
    MANUAL_DATE = 1
    NONE = 2


class PDFBuilder:
    def __init__(self, elements, properties):
        self._elements = elements
        self._table_style = TableStyle()
        self._creator = Creator()
        self._task_manager = TaskBuilder(properties)
        pdfmetrics.registerFont(TTFont(
            'News-Goth-BT', 'PdfVisualisation/news gothic bt.ttf'))

    def parse_xml_data(self, title, object_data, groups, signature):
        styles = getSampleStyleSheet()
        self.parse_title(title, styles)
        self.parse_object_data(object_data, styles)
        self.parse_questionnaire(groups, styles)
        self.parse_signature(styles, signature)

    def parse_title(self, title, styles):
        if title is not None:
            title_style = styles["Heading1"]
            title_style.alignment = 1
            self._elements.append(Paragraph(
                self._task_manager.read_settings(title.text), title_style))
            self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        else:
            print("TITLE NOT FOUND")

    def parse_object_data(self, object_data, styles):
        if object_data is not None:
            object_style = styles["Normal"]
            object_style.fontName = "News-Goth-BT"

            for item in object_data:
                row = self._creator.create_table_fixed(
                    [[Paragraph(item.tag.replace(".", " "), object_style),
                      Paragraph(item.text, object_style)]],
                    [3.0 * inch, 5.0 * inch], self._table_style.normal)
                self._elements.append(row)
            self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        else:
            print("OBJECT DATA NOT FOUND")

    def parse_questionnaire(self, groups, styles):
        if groups is not None:
            for task_group in groups:
                if task_group.get("available"):
                    if task_group.get("available") == "false":
                        continue
                print(task_group.tag, end="")
                self._task_manager.make_row(
                    self._elements, task_group, "description",
                    self._table_style.heading, "     ", styles["Heading2"])

                for sub_task_group in task_group:
                    if sub_task_group.get("available"):
                        if sub_task_group.get("available") == "false":
                            continue
                    print("\n   " + sub_task_group.tag, end="")
                    self._task_manager.make_row(
                        self._elements, sub_task_group, "description",
                        self._table_style.sub_heading, "          ",
                        styles["Heading4"])

                    for sub_task in sub_task_group:
                        if sub_task.get("available"):
                            if sub_task.get("available") == "false":
                                continue
                        for task in sub_task:
                            if task.get("available"):
                                if task.get("available") == "false":
                                    continue
                            print("\n     " + task.tag, end="")
                            self._task_manager.make_row(
                                self._elements, task, "description",
                                self._table_style.normal, "            ",
                                styles["Heading6"])

                            self._task_manager.pick_task(
                                task.get("class"), task.get("type"), task)

                            row = [self._task_manager.run()]

                            for element in row:
                                self._elements.append(element)
        else:
            print("NO TASK GROUP FOUND")

    def parse_signature(self, styles, state):
        if not isinstance(state, Signature):
            print("Use Signature class to define what to do!")
        else:
            if state != Signature.NONE:
                style_right = ParagraphStyle(
                    name='right', parent=styles['Normal'], alignment=TA_RIGHT)

                self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))

                if state == Signature.MANUAL_DATE:
                    self._elements.append(
                        Table([[Paragraph(
                            "Signature: .....................................",
                            styles["Normal"]), Paragraph(
                            "Date: .....................................",
                            style_right)]]))

                elif state == Signature.AUTO_DATE:
                    self._elements.append(
                        Table([[Paragraph(
                            "Signature: .....................................",
                            styles["Normal"]), Paragraph(
                            datetime.datetime.now().date().__str__(),
                            style_right)]]))

                self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
