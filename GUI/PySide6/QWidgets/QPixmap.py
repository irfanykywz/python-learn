# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide6.QtGui import QPixmap

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

label = QLabel()
label.setPixmap(QPixmap('QPixmap.jpg'))

layout = QVBoxLayout()
layout.addWidget(label)

window.setLayout(layout)
window.show()
app.exec()