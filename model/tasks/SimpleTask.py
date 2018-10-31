from model.tasks.Task import *
from PdfVisualisation.TableStyle import *
from reportlab.lib.styles import getSampleStyleSheet


class SimpleTask(Task):
    def __init__(self, task, properties):
        self._task = task

        self._length_dict = {"hook": [6.0], "state": [0.5, 0.5, 0.5, 0.5], "comment": [2.0]}
        self._type_task_dict = {"hook": "settings", "state": "checkbox", "comment": "text"}

        Task.__init__(self, properties, self._type_task_dict)

    def create_visualisation(self, styles):
        for key, value in self._task_dict.items():
            if self._attributes_dict[key] == "false":
                continue
            self.make_tag(key, styles)
            self._active_objects.append(self._length_dict[key])

    def make_task(self):
        styles = getSampleStyleSheet()
        table_style = TableStyle()

        for argument in self._task:
            self.add_attribute(argument)

        self.create_visualisation(styles["Italic"])

        self.resize_table()

        row = self._creator.create_table_fixed(self._desc_tasks, self._active_objects, table_style.normal)

        return row
