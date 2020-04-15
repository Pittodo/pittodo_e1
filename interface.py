import sys
from PySide2.QtWidgets import (QMainWindow, QAction, QApplication,
                                QWidget, QPushButton, QLabel,QHBoxLayout,
                                QVBoxLayout, QLineEdit, QTextEdit, QSizePolicy)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap

from classModel import Model

from debug import tic, toc

# --- Window class definition ---
class MainWindow(QMainWindow):
    def __init__(self, model):
        self.model = model
        self.app = QApplication(sys.argv)
        QMainWindow.__init__(self)

        self.load_window_config()
        self.top_menu_init()
        self.widget_init()
        toc()

# vvvv SLOTS vvvv
    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def add_task_clicked(self):
        self.model.add_task()
# ^^^^ SLOTS ^^^^
    def load_window_config(self):
        self.setWindowTitle("Pittodo")
        self.resize(800, 600)
        self.show()

    def top_menu_init(self):
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        exit_action = QAction("Exit", self)
        self.file_menu.addAction(exit_action)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)
    def widget_init(self):
        self.widget = QWidget()
        self.setCentralWidget(self.widget) # Add Widget as central window widget

        # Buttons creations
        buttonAddTask = QPushButton("Add")
        buttonDeleteTask = QPushButton("Delete")
        buttonSave = QPushButton("Save")
        buttonImport = QPushButton("Import")
        buttonExport = QPushButton("Export")
        buttonEdit = QPushButton("Edit")

        # Line edits
        taskContet = QTextEdit("TEKST")

        # Labels
        logo = QLabel("Pittodo")
        logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        logo.resize(80,60)
        pixmap = QPixmap('images/logo.png')
        logo.setPixmap(pixmap)

        # QWidget Layouts
        main = QHBoxLayout()
        navigation = QVBoxLayout()
        content = QVBoxLayout()
        singleTaskLayout = QHBoxLayout()
        taskNavigation = QVBoxLayout()

        # Widgets place in layout
        navigation.addWidget(logo)
        navigation.addWidget(buttonAddTask)
        navigation.addWidget(buttonSave)
        navigation.addWidget(buttonImport)
        navigation.addWidget(buttonExport)

        singleTaskLayout.addWidget(taskContet)
        singleTaskLayout.addLayout(taskNavigation)
        taskNavigation.addWidget(buttonDeleteTask)
        taskNavigation.addWidget(buttonEdit)
        content.addLayout(singleTaskLayout)


        main.addLayout(navigation)
        main.addLayout(content)
        self.widget.setLayout(main)

         # Signals and Slots
        buttonAddTask.clicked.connect(self.add_task_clicked)
