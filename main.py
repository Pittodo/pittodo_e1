from debug import tic, toc
import interface
from classModel import Model


if __name__ == '__main__':
    print("---------------  M A I N  -----------------")
    model = Model()
    model.add_task()
    interface.PittodoApp().run(model)
