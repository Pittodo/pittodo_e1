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

        # Symulacja bazy z modelu
        self.tasks = {1:"task1",
        2:"task2",
        3:"task3",
        4:"task4",
        5:"task5"}

        self.app = QApplication(sys.argv)
        QMainWindow.__init__(self)

        self.load_window_config()
        self.top_menu_init()
        self.widget_init()
        self.task_list_init()
        toc()

# vvvv SLOTS vvvv
    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def add_task_clicked(self):
        self.new_task()

    @Slot()
    def save_task_clicked(self, taskId, content):
        self.tasks[taskId] = content
        self.save_task(taskId)
        self.model.add_task()

    @Slot()
    def delete_task_clicked(self,id):
        self.delete_task(id)
# ^^^^ SLOTS ^^^^
    def load_window_config(self):
        '''
        Initialize window setting
        '''
        self.setWindowTitle("Pittodo")
        self.resize(800, 600)
        self.show()

    def top_menu_init(self):
        '''
        Initialize Topbar menu and it's functions
        '''
        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")
        exit_action = QAction("Exit", self)
        self.file_menu.addAction(exit_action)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.exit_app)

    def widget_init(self):
        '''
        Initialize Main widget shape
        '''
        self.widget = QWidget()
        self.setCentralWidget(self.widget) # Add Widget as central window widget

        # Buttons create for navigation bar
        buttonAddTask = QPushButton("Add")
        buttonSave = QPushButton("Save")
        buttonImport = QPushButton("Import")
        buttonExport = QPushButton("Export")
        buttonEdit = QPushButton("Edit")

        # Labels
        whenEmpty = QLabel("List is empty. Add some tasks.")
        # Logo
        logo = QLabel("Pittodo")
        logo.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        logo.resize(80,60)
        pixmap = QPixmap('images/logo.png')
        logo.setPixmap(pixmap)

        # QWidget Layouts
        main = QHBoxLayout()
        navigation = QVBoxLayout()
        self.content = QVBoxLayout()

        # Widgets place in layout
        navigation.addWidget(logo)
        navigation.addWidget(buttonAddTask)
        navigation.addWidget(buttonSave)
        navigation.addWidget(buttonImport)
        navigation.addWidget(buttonExport)

        self.content.addWidget(whenEmpty)


        main.addLayout(navigation)
        main.addLayout(self.content)
        #
        self.widget.setLayout(main)

         # Signals and Slots Connections
        buttonAddTask.clicked.connect(self.add_task_clicked)

    def task_list_init(self):
        '''
        Loading all tasks from database and creating widgets for each one.
        '''
        self.layouts = {}
        self.taskNavigations = {}
        self.contents = {}
        self.deleteButtons = {}
        self.saveButtons = {}
        for id in self.tasks:
            self.load_task(id,self.tasks[id])

    def request_new_id(self):
        '''
        Creating unique key = Id for task
        # Need to change when database will work (it creating unique id)
        '''
        try:
            uniqueTaskId = max(dict.keys(self.tasks)) + 1
        except:
            uniqueTaskId = 1

        return uniqueTaskId
        # ---------

    def new_task(self):
        '''
        Creating widgets for new task ready to edit
        '''
        taskId = self.request_new_id()
        self.tasks[taskId] = ""
        self.contents[taskId] = QTextEdit()
        self.contents[taskId].setReadOnly(False)
        self.deleteButtons[taskId] = QPushButton("Delete")
        self.saveButtons[taskId] = QPushButton("Save")

        self.layouts[taskId] = QHBoxLayout()
        self.taskNavigations[taskId] = QVBoxLayout()

        self.layouts[taskId].addWidget(self.contents[taskId])
        self.layouts[taskId].addLayout(self.taskNavigations[taskId])
        self.taskNavigations[taskId].addWidget(self.deleteButtons[taskId])
        self.taskNavigations[taskId].addWidget(self.saveButtons[taskId])
        self.content.addLayout(self.layouts[taskId])

        self.saveButtons[taskId].clicked.connect(lambda: self.save_task_clicked(taskId, self.contents[taskId].toPlainText()))
        self.deleteButtons[taskId].clicked.connect(lambda: self.delete_task_clicked(taskId))

    def save_task(self, taskId):
        '''
        Saving task on list which means changing control button from save to
        edit and freeze edit window
        '''
        buttonEdit = QPushButton("Edit")
        self.taskNavigations[taskId].addWidget(buttonEdit)
        self.contents[taskId].setReadOnly(True)
        self.saveButtons[taskId].setParent(None)

    def load_task(self, taskId, taskContent):
        '''
        Creating widgets for task which are arleady exist in database.
        '''
        self.contents[taskId] = QTextEdit(str(taskContent))
        self.contents[taskId].setReadOnly(True)
        self.deleteButtons[taskId] = QPushButton("Delete")
        buttonEdit = QPushButton("Edit")

        self.layouts[taskId] = QHBoxLayout()
        self.taskNavigations[taskId] = QVBoxLayout()

        self.layouts[taskId].addWidget(self.contents[taskId])
        self.layouts[taskId].addLayout(self.taskNavigations[taskId])
        self.taskNavigations[taskId].addWidget(self.deleteButtons[taskId])
        self.taskNavigations[taskId].addWidget(buttonEdit)
        self.content.addLayout(self.layouts[taskId])

        self.deleteButtons[taskId].clicked.connect(lambda: self.delete_task_clicked(taskId))

    def delete_task(self, taskId):
        '''
        Removing controls for specific task and removing it from database
        '''
        outer = self.layouts[taskId]
        inner = self.taskNavigations[taskId]
        for i in reversed(range(inner.count())):
            inner.itemAt(i).widget().setParent(None)
        inner.setParent(None)
        for i in reversed(range(outer.count())):
            outer.itemAt(i).widget().setParent(None)
        outer.setParent(None)
        del self.layouts[taskId]
        del self.taskNavigations[taskId]
        del self.contents[taskId]
        del self.tasks[taskId]
        del self.deleteButtons[taskId]

    def edit_task(self):
        pass
