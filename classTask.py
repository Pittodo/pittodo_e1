from enum import Enum


class Task:

    def __init__(self):
        self.id = 0
        self.content = ""
        self.status = TaskStatus.TODO

    def set_status(self, status_name):
        self.status = status_name

    def get_status(self):
        return self.status

    def set_content(self, content):
        self.content = content

    def get_content(self):
        return self.content

    def __eq__(self, other):
        return (self.content == other.content) and (self.id == other.id)


class TaskStatus(Enum):
    TODO = 0
    DOING = 1
    DONE = 2
