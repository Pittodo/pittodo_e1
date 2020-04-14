from debug import tic, toc
tic()  # for debug window loading time
import sys
from PySide2.QtWidgets import QApplication
import interface
from classModel import Model


if __name__ == '__main__':

    print("---------------  M A I N  -----------------")
    model = Model()
    model.add_task()
    app = QApplication(sys.argv)
    widget = interface.PittodoMainWidget()
    window = interface.MainWindow(widget)



    sys.exit(app.exec_())
