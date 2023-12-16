# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QSpinBox

def sliderAct(data):
    print('checked :', data)

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("pyside6 learn")

slider = QSpinBox()
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(10)
slider.valueChanged.connect(sliderAct)

window.setCentralWidget(slider)
window.show()

app.exec()