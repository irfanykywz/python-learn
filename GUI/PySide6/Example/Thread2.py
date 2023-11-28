from PySide6 import QtCore, QtWidgets
import sys

class Worker(QtCore.QObject):

    retrieved = QtCore.Signal(object)

    def __init__(self):
        super().__init__()
        self._i = 0

    def onRetrieve(self):
        def incAndEmit():
            self._i += 1
            self.retrieved.emit(self._i)
        QtCore.QTimer.singleShot(100, incAndEmit)

class Ui(QtWidgets.QWidget):

    retrieve = QtCore.Signal()

    def __init__(self, parent = None):
        super().__init__(parent)

        # ui initialisation
        startButton = QtWidgets.QPushButton("start")
        stopButton = QtWidgets.QPushButton("stop")
        startButton.clicked.connect(self.onStartClicked)
        stopButton.clicked.connect(self.onStopClicked)
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(startButton)
        layout.addWidget(stopButton)
        self.setLayout(layout)

        worker = Worker()
        thread = QtCore.QThread()
        self.retrieve.connect(worker.onRetrieve)
        worker.retrieved.connect(self.onRetrieved)
        worker.moveToThread(thread)
        thread.start()

        self._thread = thread # protect from destroying by gc
        self._worker = worker # protect from destroying by gc
        self._stop = False

    def onStartClicked(self):
        self._stop = False
        self.retrieve.emit()

    def onStopClicked(self):
        self._stop = True

    def onRetrieved(self, data):
        # process data
        print("onRetrieved", data)
        if self._stop:
            return
        self.retrieve.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui()
    ui.show()
    app.exec()