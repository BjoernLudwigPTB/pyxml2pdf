from reportlab.platypus import TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from model.tasks.TaskBuilder import *
from PdfVisualisation.TableStyle import *
from PdfVisualisation.FlowableRect import *
from reportlab.lib.enums import TA_RIGHT


class PDFBuilder:
    def __init__(self, elements, properties):
        self._elements = elements
        self._table_style = TableStyle()
        self._creator = Creator()
        self._task_manager = TaskBuilder(properties)

    def parse_xml_data(self, title, object_data, groups):
        styles = getSampleStyleSheet()
        self.parse_title(title, styles)
        self.parse_object_data(object_data, styles)
        self.parse_questionnaire(groups, styles)
        self.parse_signature(styles)

    def parse_title(self, title, styles):
        title_style = styles["Heading1"]
        title_style.alignment = 1
        self._elements.append(Paragraph(self._task_manager.read_settings(title.text), title_style))
        self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    def parse_object_data(self, object_data, styles):
        object_style = styles["Normal"]
        object_style.fontName = "Theano-Modern"

        for item in object_data:
            row = self._creator.create_table_fixed([[Paragraph(item.tag.replace(".", " "), object_style),
                                                     Paragraph(item.text, object_style)]],
                                                   [3.0 * inch, 5.0 * inch], self._table_style.normal)
            self._elements.append(row)
        self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))

    def parse_questionnaire(self, groups, styles):
        for task_group in groups:
            if task_group.get("available"):
                if task_group.get("available") == "false":
                    continue
            print(task_group.tag, end="")
            self._task_manager.make_row(self._elements, task_group, "description", self._table_style.heading,
                              "     ", styles["Heading2"])

            for sub_task_group in task_group:
                if sub_task_group.get("available"):
                    if sub_task_group.get("available") == "false":
                        continue
                print("\n   " + sub_task_group.tag, end="")
                self._task_manager.make_row(self._elements, sub_task_group, "description",
                                            self._table_style.sub_heading, "          ", styles["Heading4"])

                for sub_task in sub_task_group:
                    if sub_task.get("available"):
                        if sub_task.get("available") == "false":
                            continue
                    for task in sub_task:
                        if task.get("available"):
                            if task.get("available") == "false":
                                continue
                        print("\n     " + task.tag, end="")
                        self._task_manager.make_row(self._elements, task, "description", self._table_style.normal,
                                      "            ", styles["Heading6"])

                        self._task_manager.pick_task(task.get("class"), task.get("type"), task)

                        row = []
                        row.append(self._task_manager.run())

                        for element in row:
                            self._elements.append(element)

    def parse_signature(self, styles):
        style_right = ParagraphStyle(name='right', parent=styles['Normal'], alignment=TA_RIGHT)

        self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        self._elements.append(Table([[Paragraph("Signature: .....................................", styles["Normal"]),
                                      Paragraph("Date: .....................................", style_right)]]))
        self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
