import sys
import interface
from debug import tic, toc
from classModel import Model
tic()  # for debug window loading time

if __name__ == '__main__':

    print("---------------  M A I N  -----------------")
    model = Model()
    model.add_task() # Only for testing
    window = interface.MainWindow(model)
    sys.exit(window.app.exec_())
