from PySide2.QtWidgets import (QMainWindow, QAction, QApplication,
                                QWidget, QPushButton, QLabel,QHBoxLayout,
                                QVBoxLayout)
from PySide2.QtCore import QObject, Signal, Slot

from classModel import Model

from debug import tic, toc

# --- Widget inside window definition ---
class PittodoMainWidget(QWidget):
    def __init__(self):
        super().__init__()
        # Create object of Model in the widget
        self.model = Model()
        # Buttons creations
        self.buttonAddTask = QPushButton("Add")
        self.buttonDeleteTask = QPushButton("Delete")
        self.buttonSave = QPushButton("Save")
        self.buttonImport = QPushButton("Import")
        self.buttonExport = QPushButton("Export")

        # Labels
        self.text = QLabel("Pittodo")
        # QWidget Layouts
        self.left = QVBoxLayout()

        # Buttons connect with layout
        self.left.addWidget(self.buttonAddTask)
        self.left.addWidget(self.buttonDeleteTask)
        self.left.addWidget(self.buttonSave)
        self.left.addWidget(self.buttonImport)
        self.left.addWidget(self.buttonExport)

        self.left.addWidget(self.text)
        self.setLayout(self.left)

         # Signals and Slots
        self.buttonAddTask.clicked.connect(self.add_task_clicked)

    @Slot()
    def add_task_clicked(self):
        self.model.add_task()


# --- Window class definition ---
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

# def add_task(self):
#     print("[PittodoApp] add_task()")
#     self.model.add_task()
