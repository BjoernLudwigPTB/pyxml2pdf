from reportlab.lib.pagesizes import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator
from PdfVisualisation.TableStyle import TableStyle
from model.courses.CourseBuilder import CourseBuilder


class PDFBuilder:
    def __init__(self, elements, properties):
        self._elements = elements
        self._table_style = TableStyle()
        self._creator = Creator()
        self._course_manager = CourseBuilder(properties)
        pdfmetrics.registerFont(TTFont(
            'News-Goth-BT', 'PdfVisualisation/news gothic bt.ttf'))

    def parse_xml_data(self, object_data, courses):
        styles = getSampleStyleSheet()
        self.parse_title('title.no1', styles)
        self.parse_courses(courses, styles)

    def parse_title(self, title, styles):
        """
        Determine the desired title for the table and create a first
        paragraph for it in the pdf.

        Parameters
        ----------
        :param str title: the title of the table
        :param reportlab.lib.styles.StyleSheet1 styles: all styles in the pdf
        """
        if title is not None:
            title_style = styles["Heading1"]
            title_style.alignment = 1
            self._elements.append(Paragraph(
                self._course_manager.read_settings(title), title_style))
            self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        else:
            print("TITLE NOT FOUND")

    def parse_course_data(self, course_data, styles):
        if course_data is not None:
            course_style = styles["Normal"]
            course_style.fontName = "News-Goth-BT"

            for item in course_data:
                if item.text:
                    row = self._creator.create_table_fixed(
                        [[Paragraph(item.tag, course_style),
                          Paragraph(item.text, course_style)]],
                        [3.0 * inch, 5.0 * inch], self._table_style.normal)
                    self._elements.append(row)
            self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        else:
            print("OBJECT DATA NOT FOUND")

    def parse_courses(self, courses, styles):
        if courses is not None:
            for course in courses:
                self.parse_course_data(course, styles)
                print(course.tag, end="")
                self._course_manager.make_row(
                    self._elements, course, "description",
                    self._table_style.heading, "     ", styles["Heading2"])

                for sub_task_group in course:
                    if sub_task_group.get("available"):
                        if sub_task_group.get("available") == "false":
                            continue
                    print("\n   " + sub_task_group.tag, end="")
                    self._course_manager.make_row(
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
                            self._course_manager.make_row(
                                self._elements, task, "description",
                                self._table_style.normal, "            ",
                                styles["Heading6"])

                            self._course_manager.pick_course(
                                task.get("class"), task.get("type"), task)

                            row = [self._course_manager.run()]

                            for element in row:
                                self._elements.append(element)
        else:
            print("NO TASK GROUP FOUND")
