from reportlab.lib.pagesizes import mm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.pdfmetrics import registerFont, registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph

from PdfVisualisation.Creator import Creator
from PdfVisualisation.TableStyle import TableStyle
from model.courses.CourseBuilder import CourseBuilder


class PDFBuilder:
    def __init__(self, elements, properties):
        self._elements = elements
        self._creator = Creator()
        self._course_manager = CourseBuilder(properties)
        self._table_style = TableStyle(self._course_manager.read_settings(
            'table_width'))
        PDFBuilder._set_font_family()

    @staticmethod
    def _set_font_family():
        registerFont(TTFont('NewsGothBT',
                            'PdfVisualisation/NewsGothicBT-Roman.ttf'))
        registerFont(TTFont('NewsGothBT_Bd',
                            'PdfVisualisation/NewsGothicBT-Bold.ttf'))
        registerFont(TTFont('NewsGothBT_Italic',
                            'PdfVisualisation/NewsGothicBT-Italic.ttf'))
        registerFont(TTFont('NewsGothBT_BoldItalic',
                            'PdfVisualisation/NewsGothicBT-BoldItalic.ttf'))
        registerFontFamily(
            'NewsGothBT', normal='NewsGothBT', bold='NewsGothBT_Bd',
            italic='NewsGothBT_Italic',
            boldItalic='NewsGothBT_BoldItalic')

    def parse_xml_data(self, object_data, courses):
        # Get styles for all headings, texts, etc. from sample
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
            title_style.fontName = 'NewsGothBT'
            self._elements.append(Paragraph(
                self._course_manager.read_settings(title), title_style))
            self._elements.append(Paragraph("<br/><br/>", styles["Normal"]))
        else:
            print("TITLE NOT FOUND")

    def parse_course_data(self, course_data, styles):
        if course_data is not None:
            course_style = styles["Normal"]
            # Adapt font to specification
            course_style.fontName = 'NewsGothBT'
            course_style.bulletFontName = 'NewsGothBT'
            # Adapt fontsize to specification
            course_style.fontSize = 7
            heading = ['Bezeichnung', 'Kurstermin', 'Beschreibung',
                       'Kurskosten', 'Ort1', 'Kursleiter', 'Kursart',
                       'Zielgruppe']
            i = 1
            row = []
            for item in course_data:
                if item.tag in heading:
                    if item.text:
                        text = item.text
                    else:
                        text = ""
                    row.append(Paragraph(text, course_style))
            final_row = self._creator.create_table_fixed([row],
                [20 * mm, 16 * mm, 50 * mm, 13 * mm, 20 * mm, 20 * mm,
                 8 * mm, 20 * mm], self._table_style.normal)
            self._elements.append(final_row)
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
