from PySide2 import QtCore, QtGui, QtWidgets, QtQuickWidgets
from taskWidget import TaskWidget


app = QtWidgets.QApplication([])
tw = TaskWidget()
tw.show()
app.exec_()
