# https://stackoverflow.com/questions/45175427/pyqt5-run-function-after-displaying-window
import os
import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QWidget
from PySide6.QtCore import QUrl, QEventLoop, QThread, QObject, Slot, Signal
from PySide6.QtWebEngineWidgets import QWebEngineView

class time_consuming_function(QObject):
    def __init__(self, widget):
        super(time_consuming_function, self).__init__()
        self.widget = widget
        self.run_trigger.connect(self.run)

    run_trigger = Signal(int, int)
    @Slot(int, int)
    def run(self, int1, int2):
        print("In Time Consuming Function")
        for i in range(100000000):
            i*i
        print("Finished with Time Consuming Function")
        self.widget.someTrigger.emit([1, 2, 3])

class WebPage(QWebEngineView):
    def __init__(self):
        QWebEngineView.__init__(self)
        self.load(QUrl("https://www.google.com"))
        self.loadFinished.connect(self._on_load_finished)

        self.someTrigger.connect(self.gui_response)

        self.thread = QThread()
        self.thread.start()
        self.consume = time_consuming_function(self)
        self.consume.moveToThread(self.thread)
        self.consume.run_trigger.emit(1,1)

    someTrigger = Signal(list)

    def _on_load_finished(self):
        print("Finished Loading")

    def gui_response(self, data):
        print("Responding to GUI: ", str(data))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    web = WebPage()
    web.show()
    sys.exit(app.exec_())  