from reportlab.lib.styles import getSampleStyleSheet

from PdfVisualisation.TableStyle import TableStyle
from model.courses.Course import Course


class SimpleCourse(Course):
    def __init__(self, course, properties):
        self._course = course

        self._length_dict = {
            "hook": [6.0], "state": [0.5, 0.5, 0.5, 0.5], "comment": [2.0]}
        self._type_course_dict = {
            "hook": "settings", "state": "checkbox", "comment": "text"}

        Course.__init__(self, properties, self._type_course_dict)

    def create_visualisation(self, styles):
        for key, value in self._course_dict.items():
            if self._attributes_dict[key] == "false":
                continue
            self.make_tag(key, styles)
            self._active_objects.append(self._length_dict[key])

    def make_course(self):
        styles = getSampleStyleSheet()
        table_style = TableStyle()

        for argument in self._course:
            self.add_attribute(argument)

        self.create_visualisation(styles["Italic"])

        self.resize_table()

        row = self._creator.create_table_fixed(
            self._desc_courses, self._active_objects, table_style.normal)

        return row
