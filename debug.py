import time
from classModel import Model


def TicTocGenerator():
    # Generator that returns time differences
    ti = 0           # initial time
    tf = time.time()  # final time
    while True:
        ti = tf
        tf = time.time()
        yield tf-ti  # returns the time difference


TicToc = TicTocGenerator()  # create an instance of the TicTocGen generator


def toc(tempBool=True):
    # Prints the time difference yielded by generator instance TicToc
    tempTimeInterval = next(TicToc)
    if tempBool:
        print("Elapsed time: %f seconds.\n" % tempTimeInterval)


def tic():
    # Records a time in TicToc, marks the beginning of a time interval
    toc(False)


def print_database(filename):
    m = Model()
    m.settings['db_path'] = filename
    m.load_tasks()
    for it in range(len(m.tasks)):
        print("\nTASK     {} -----------------------".format(it))
        print("CONTENT: {}".format(m.tasks[it].get_content()))
        print("STATUS:  {}".format(m.tasks[it].get_status()))
