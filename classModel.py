from classDatabaseConnector import DatabaseConnector
import copy


class Model:
    settings_path = "settings.txt"

    def __init__(self):
        self.tasks = []
        self.settings = {}

    def add_task(self, task):
        print("[Model] add_task()")
        self.tasks.append(copy.copy(task))

    def del_task(self, task_id):
        del self.tasks[task_id]

    def get_task(self, task_id):
        return self.tasks[task_id]

    def get_last_task_id(self):
        return len(self.tasks)-1

    def save_tasks(self):
        DatabaseConnector(self.settings['db_path']).save(self.tasks)

    def load_tasks(self):
        self.tasks = DatabaseConnector(self.settings['db_path']).load()

    def save_settings(self):
        DatabaseConnector(self.settings_path).save(self.settings)

    def load_settings(self):
        self.settings = DatabaseConnector(self.settings_path).load()
