from classDatabaseConnector import DatabaseConnector
import copy
from classTask import Task


class Model:
    SETTINGS_PATH = "settings.dat"
    MAX_ID = 9999

    def __init__(self):
        self.tasks = []
        self.settings = {}

    def add_task(self, task):
        self.tasks.append(copy.copy(task))

    def add_empty_task(self, task_id):
        t = Task()
        t.id = self.find_free_id()
        self.tasks.append(t)
        return t.id

    def del_task(self, task_id):
        for i in range(len(self.tasks)):
            if(self.tasks[i].id == task_id):
                del self.tasks[i]
                break

    def get_task_index(self, task):
        for i in range(len(self.tasks)):
            if(task == self.tasks[i]):
                return i
        return False

    def find_free_id(self):
        for id in range(0, self.MAX_ID):
            for task in self.tasks:
                if id == task.id:
                    continue
            break
        return id

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        return False

    def save_tasks(self):
        DatabaseConnector(self.settings['db_path']).save(self.tasks)

    def load_tasks(self):
        self.tasks = DatabaseConnector(self.settings['db_path']).load()

    def save_settings(self):
        DatabaseConnector(self.SETTINGS_PATH).save(self.settings)

    def load_settings(self):
        self.settings = DatabaseConnector(self.SETTINGS_PATH).load()
