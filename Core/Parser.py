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
        registerFont(TTFont('NewsGothBT_Bold',
                            'PdfVisualisation/NewsGothicBT-Bold.ttf'))
        registerFont(TTFont('NewsGothBT_Italic',
                            'PdfVisualisation/NewsGothicBT-Italic.ttf'))
        registerFont(TTFont('NewsGothBT_BoldItalic',
                            'PdfVisualisation/NewsGothicBT-BoldItalic.ttf'))
        registerFontFamily(
            'NewsGothBT', normal='NewsGothBT', bold='NewsGothBT_Bold',
            italic='NewsGothBT_Italic',
            boldItalic='NewsGothBT_BoldItalic')

    @staticmethod
    def _get_course_data(course_data, course_data_tags):
        """
        Forms a string of the descriptive texts for all desired course tags
        by concatenating them seperated by ' + '.

        :param xml.etree.ElementTree.Element course_data: the course data
            from where the texts shall be extracted
        :param list(str) course_data_tags: list of all tags for which the
            descriptive texts is wanted
        :return str: the texts of all tags under the current course
        """
        course_data_string = ""
        for tag in course_data_tags:
            data_string = course_data.findtext(tag)
            if data_string:
                if course_data_string:
                    course_data_string += " - " + data_string
                else:
                    course_data_string = data_string
        return course_data_string

    @staticmethod
    def _parse_prerequisites(personal, material, financial, offers):
        """
        Determine all prerequisites and assemble a string accordingly.

        :param str material: material prerequisite xml text
        :param str personal: personal prerequisite xml text
        :param str financial: financial prerequisite xml text
        :param str offers: xml text of what is included in the price
        :return str: the text to insert in prerequisite column
        the current course
        """
        if personal:
            personal_string = 'a) ' + personal + '<br/>'
        else:
            personal_string = 'a) keine <br/>'

        if material:
            material_string = 'b) ' + material + '<br/>'
        else:
            material_string = 'b) keine <br/>'

        if financial:
            financial_string = 'c) ' + financial + ' € (' + offers + ')'
        else:
            financial_string = 'c) keine'
        return personal_string + material_string + financial_string

    @staticmethod
    def _parse_date(self, date):
        """
        Determine the correct date for printing.

        :param str date: xml tag for relevant date.
        :return str: the text to insert in date column of the current course
        """
        if date:
            date_string = date
        return date_string

    def parse_xml_data(self, object_data, courses):
        # Get styles for all headings, texts, etc. from sample
        styles = getSampleStyleSheet()
        styles["Normal"].fontSize = 7
        styles["Normal"].leading = styles["Normal"].fontSize * 1.2
        styles["Normal"].fontName = 'NewsGothBT'
        styles["Italic"].fontSize = styles["Normal"].fontSize
        styles["Italic"].leading = styles["Italic"].fontSize * 1.2
        styles["Italic"].fontName = 'NewsGothBT_Italic'
        styles["Heading1"].fontSize = styles["Normal"].fontSize
        styles["Heading1"].leading = styles["Heading1"].fontSize * 1.2
        styles["Heading1"].fontName = 'NewsGothBT_Bold'
        self.parse_courses(courses, styles)

    def parse_course_data(self, course_data, styles):
        if course_data is not None:
            heading = dict(
                Bezeichnung='Bezeichnung', Kurstermin='Termin',
                Beschreibung='Beschreibung', Kurskosten='Kosten', Ort1='Ort',
                Kursleiter='Leitung', Kursart='Art', Zielgruppe='Zielgruppe')
            columns = [
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Kursart']), styles["Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['TerminDatumVon1', 'TerminDatumBis1']),
                    styles["Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Ort1']), styles["Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Kursleiter']), styles["Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Bezeichnung', 'Bezeichnung2',
                                  'Beschreibung']), styles[
                    "Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Zielgruppe']), styles["Normal"]),
                Paragraph(PDFBuilder._parse_prerequisites(
                    PDFBuilder._get_course_data(
                        course_data, ['Voraussetzung']),
                    PDFBuilder._get_course_data(course_data, ['Ausrüstung']),
                    PDFBuilder._get_course_data(course_data, ['Kurskosten']),
                    PDFBuilder._get_course_data(course_data, ['Leistungen'])),
                    styles["Normal"]),
                Paragraph(PDFBuilder._get_course_data(
                    course_data, ['Bemerkungen']), styles["Normal"])]
            row = self._creator.create_table_fixed(
                [columns], [8*mm, 18*mm, 20*mm, 18*mm, 40*mm, 21*mm,
                            27*mm, 26*mm], self._table_style.normal)
            self._elements.append(row)
        else:
            print("OBJECT DATA NOT FOUND")

    def parse_courses(self, courses, styles):
        if courses is not None:
            for course in courses:
                self.parse_course_data(course, styles)
                print(course.findtext('Bezeichnung'), end="")
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
