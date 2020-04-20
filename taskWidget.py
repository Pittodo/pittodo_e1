from PySide2.QtWidgets import (QWidget, QPushButton, QLabel, QHBoxLayout,
                               QVBoxLayout, QLineEdit, QTextEdit, QSizePolicy,
                               QCheckBox)
from PySide2.QtQuickWidgets import QQuickWidget
from PySide2.QtCore import QUrl


class TaskStatusWidget(QCheckBox):
    def __init__(self, *args, **kwargs):
        super(TaskStatusWidget, self).__init__(*args, **kwargs)
        self.setTristate(True)


class TaskContentWidget(QTextEdit):
    def __init__(self, *args, **kwargs):
        super(TaskContentWidget, self).__init__(*args, **kwargs)


class TaskActionButtons(QWidget):
    def __init__(self, *args, **kwargs):
        super(TaskActionButtons, self).__init__(*args, **kwargs)
        layout = QHBoxLayout()
        b1 = QPushButton()
        b2 = QPushButton()
        layout.addWidget(b1)
        layout.addWidget(b2)
        self.setLayout(layout)


class TaskWidget(QQuickWidget):
    def __init__(self, *args, **kwargs):
        super(TaskWidget, self).__init__(*args, **kwargs)
        self.setSource(QUrl.fromLocalFile('taskWidgetStyle.qml'))
        layout = QHBoxLayout()
        task_status = TaskStatusWidget()
        task_content = TaskContentWidget()
        task_action_buttons = TaskActionButtons()
        layout.addWidget(task_status)
        layout.addWidget(task_content)
        layout.addWidget(task_action_buttons)
        self.setLayout(layout)
