# https://gist.github.com/chipolux/a600d2a31b6811d553651822f89c9e39
# A simple example of using a QTimer to create a debounce on a line edit.
#   For things like search fields, etc.

from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QWidget, QLineEdit, QApplication, QVBoxLayout


class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.line_edit = QLineEdit()
        layout.addWidget(self.line_edit)

        self.debounce = QTimer()
        self.debounce.setInterval(500)
        self.debounce.setSingleShot(True)
        self.debounce.timeout.connect(self.debounced)

        self.line_edit.textChanged.connect(self.debounce.start)

    def debounced(self):
        print(self.line_edit.text())


app = QApplication([])
widget = Widget()
widget.resize(800, 600)
widget.show()
app.exec_()