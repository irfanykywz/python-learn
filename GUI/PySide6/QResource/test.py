import sys
from PySide6 import QtGui, QtWidgets
import resources

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World")
        self.button = QtWidgets.QPushButton("My button")

        icon = QtGui.QIcon(":/icons/arrow-bottom.png")
        self.button.setIcon(icon)

        self.setCentralWidget(self.button)

        self.show()


app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
app.exec_()