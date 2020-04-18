import sys
import interface
import newInterface
from debug import tic
from classModel import Model
tic()  # for debug window loading time

if __name__ == '__main__':

    print("---------------  M A I N  -----------------")
    model = Model()
    # window = interface.MainWindow(model)
    # sys.exit(window.app.exec_())
    window = newInterface.MainWindow(model)

    if not window.engine.rootObjects():
        sys.exit(-1)
    sys.exit(window.app.exec_())
