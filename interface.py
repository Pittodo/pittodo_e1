from PySide2.QtWidgets import (QMainWindow, QAction, QApplication,
                                QWidget, QPushButton, QLabel,QHBoxLayout,
                                QVBoxLayout)
from PySide2.QtCore import QObject, Signal, Slot

from classModel import Model

from debug import tic, toc

class PittodoMainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.buttonAddTask = QPushButton("AddTask")
        self.text = QLabel("Pittodo")
        # QWidget Layout
        self.left = QVBoxLayout()
        self.left.addWidget(self.buttonAddTask)
        self.left.addWidget(self.text)
        self.setLayout(self.left)

         # Signals and Slots
        self.buttonAddTask.clicked.connect(self.add_task)

    @Slot()
    def add_task():
        Model.add_task()


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)
        self.setWindowTitle("Pittodo")
        self.resize(800, 600)

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
        self.file_menu.addAction(exit_action)
        # Add Widget as central window widget
        self.setCentralWidget(widget)
        self.show()
        toc()

    @Slot()
    def exit_app(self, checked):
        QApplication.quit()


def run(self, model):
    self.model = model

def add_task(self):
    print("[PittodoApp] add_task()")
    self.model.add_task()
