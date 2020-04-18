import sys
from PySide2.QtCore import Qt, QObject, Signal, Slot, Property
from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine

class Manager(QObject):
    currentValueChanged = Signal()

    def __init__(self):
        QObject.__init__(self)
        self.m_currentValue = 0.0
        self.currentValueChanged.connect(self.on_currentValueChanged)

    @Property(float, notify=currentValueChanged)
    def currentValue(self):
        return self.m_currentValue

    @currentValue.setter
    def setCurrentValue(self, val):
        if self.m_currentValue == val:
            return
        self.m_currentValue = val
        self.currentValueChanged.emit()

    @Slot()
    def on_currentValueChanged(self):
        print(self.m_currentValue)

class MainWindow():
    def __init__(self, model):
        self.app = QGuiApplication(sys.argv)

        self.engine = QQmlApplicationEngine()
        manager = Manager()
        ctx = self.engine.rootContext()
        ctx.setContextProperty("Manager", manager)
        self.engine.load('style/interface.qml')






    def exit_app(self, checked):
        pass
