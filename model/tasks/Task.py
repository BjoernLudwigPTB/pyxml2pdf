from model.tasks.TaskBuilder import *
from PdfVisualisation.Creator import *
from reportlab.platypus import Paragraph


class Task:
    def __init__(self, properties, type_task):
        self._creator = Creator()
        self._task_manager = TaskBuilder(properties)

        self._desc_tasks = [[]]
        self._active_objects = []

        self._task_dict = {}
        self._attributes_dict = {}
        self._type_task_dict = type_task

    def add_attribute(self, task):
        self._task_dict.update({task.tag: task.text})
        if task.get("available"):
            self._attributes_dict.update({task.tag: task.get("available")})
        else:
            self._attributes_dict.update({task.tag: "true"})

    def make_tag(self, key, styles):
        if self._type_task_dict[key] == "settings":
            self._desc_tasks[0].append(Paragraph(self._task_manager.read_settings(self._task_dict[key]), styles))
        elif self._type_task_dict[key] == "checkbox":
            self._creator.make_checkbox_form(self._task_dict[key], self._desc_tasks, styles)
        elif self._type_task_dict[key] == "text":
            self._desc_tasks[0].append(Paragraph(self._task_dict[key], styles))

    def resize_table(self):
        if sum(sum(self._active_objects, [])) > 8.0:
            m = max(self._active_objects)
            index = [i for i, j in enumerate(self._active_objects) if j == m]
            self._active_objects[index[0]][0] = self._active_objects[index[0]][0] - (sum(sum(self._active_objects, [])) - 8.0)

        elif sum(sum(self._active_objects, [])) < 8.0:
            m = min(self._active_objects)
            index = [i for i, j in enumerate(self._active_objects) if j == m]
            self._active_objects[index[0]][0] = self._active_objects[index[0]][0] + (8.0 - sum(sum(self._active_objects, [])))

        self._active_objects = [item for sublist in self._active_objects for item in sublist]

        for i in range(self._active_objects.__len__()):
            self._active_objects[i] = self._active_objects[i] * inch