import sys
from PySide2.QtWidgets import (QMainWindow, QAction, QApplication,
                                QWidget, QPushButton, QLabel,QHBoxLayout,
                                QVBoxLayout, QLineEdit, QTextEdit, QSizePolicy)
from PySide2.QtCore import QObject, Signal, Slot
from PySide2.QtGui import QPixmap
import debug


# --- Window class definition ---
class MainWindow(QMainWindow):
    def __init__(self, model):

        # Application
        self.app = QApplication(sys.argv)
        QMainWindow.__init__(self)

        # Window config
        self.load_window_config()

        # Model
        self.model = model
        self.model.load_settings()

        # Components initialization
        self.top_menu_init()
        self.widget_init()
        self.task_list_init()

        # Debug
        debug.toc()

# vvvv SLOTS vvvv
    @Slot()
    def exit_app(self, checked):
        QApplication.quit()

    @Slot()
    def add_task_clicked(self):
        self.new_task()

    @Slot()
    def save_task_clicked(self, taskId, content):
        self.save_task(taskId)


    @Slot()
    def delete_task_clicked(self, id):
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
        self.setCentralWidget(self.widget)  # Add Widget as central window widget

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
        logo.resize(80, 60)
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
        self.model.load_tasks()
        self.layouts = {}
        self.taskNavigations = {}
        self.contents = {}
        self.deleteButtons = {}
        self.saveButtons = {}
        for index in range(len(self.model.tasks)):
            task = self.model.tasks[index]
            self.load_task(task.id, task.get_content())

    def new_task(self):
        '''
        Creating widgets for new task ready to edit
        '''
        task_id = self.model.add_empty_task()
        # self.tasks[taskId] = ""
        self.contents[task_id] = QTextEdit()
        self.contents[task_id].setReadOnly(False)
        self.deleteButtons[task_id] = QPushButton("Delete")
        self.saveButtons[task_id] = QPushButton("Save")

        self.layouts[task_id] = QHBoxLayout()
        self.taskNavigations[task_id] = QVBoxLayout()

        self.layouts[task_id].addWidget(self.contents[task_id])
        self.layouts[task_id].addLayout(self.taskNavigations[task_id])
        self.taskNavigations[task_id].addWidget(self.deleteButtons[task_id])
        self.taskNavigations[task_id].addWidget(self.saveButtons[task_id])
        self.content.addLayout(self.layouts[task_id])

        self.saveButtons[task_id].clicked.connect(lambda: self.save_task_clicked(task_id, self.contents[task_id].toPlainText()))
        self.deleteButtons[task_id].clicked.connect(lambda: self.delete_task_clicked(task_id))

    def save_task(self, task_id):
        '''
        Saving task on list which means changing control button from save to
        edit and freeze edit window
        '''
        buttonEdit = QPushButton("Edit")
        self.taskNavigations[task_id].addWidget(buttonEdit)
        self.contents[task_id].setReadOnly(True)
        self.saveButtons[task_id].setParent(None)
        content_string = self.contents[task_id].toPlainText()
        task = self.model.get_task(task_id)
        task.set_content(content_string)
        self.model.save_tasks()

    def load_task(self, taskId, taskContent):
        '''
        Creating widgets for task which are exists in the database.
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

    def delete_task(self, task_id):
        '''
        Removing controls for specific task and removing it from database
        '''
        outer = self.layouts[task_id]
        inner = self.taskNavigations[task_id]
        for i in reversed(range(inner.count())):
            inner.itemAt(i).widget().setParent(None)
        inner.setParent(None)
        for i in reversed(range(outer.count())):
            outer.itemAt(i).widget().setParent(None)
        outer.setParent(None)
        del self.layouts[task_id]
        del self.taskNavigations[task_id]
        del self.contents[task_id]
        del self.deleteButtons[task_id]
        self.model.del_task(task_id)
        self.model.save_tasks()

    def edit_task(self):
        pass
