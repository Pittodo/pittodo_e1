from PySide2 import QtCore, QtGui, QtWidgets
from taskWidget import TaskWidget


app = QtWidgets.QApplication([])
tw = TaskWidget()
tw.show()
app.exec_()
