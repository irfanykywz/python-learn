# https://stackoverflow.com/questions/24976885/how-to-limit-qthread-number
 
from PySide6 import QtCore, QtGui, QtWidgets
import queue
import time

class Signal(QtCore.QObject):
    sig = QtCore.Signal(str)

class Worker(QtCore.QRunnable):
    def __init__(self, theQueue, sig):
        QtCore.QRunnable.__init__(self)
        self.theQueue = theQueue
        self.signal = sig

    def run(self):
        while True:			
            task = self.theQueue.get()
            if task is None:
                self.theQueue.task_done()
                return
            # run task
            print(task)

            time.sleep(1)
            # print(task)
            # self.signal.sig.emit(task)
            self.theQueue.task_done()

def result_callback(result):
    print("Got {}".format(result))


MAX_THREADS = 4
def launch_threads():
    theQueue = queue.Queue()
    pool = QtCore.QThreadPool()
    pool.setMaxThreadCount(MAX_THREADS)

    # create 4 thread 
    for thread in range(MAX_THREADS): 
        sig = Signal()
        sig.sig.connect(result_callback)
        pool.start(Worker(theQueue, sig))

    # insert task
    for i in range(100): # Sending more values than there are threads
        theQueue.put(i)

    # Tell the threads in the pool to finish
    for i in range(MAX_THREADS):
        theQueue.put(None)

    pool.waitForDone()
    QtCore.QTimer.singleShot(0, QtWidgets.QApplication.instance().exit)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    QtCore.QTimer.singleShot(0, launch_threads)
    app.exec_()