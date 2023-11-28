# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QTabWidget, QPushButton, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

tab_w = QTabWidget()

#tab1
w1 = QWidget()
label = QLabel('Name')
line = QLineEdit()
w1_form = QHBoxLayout()
w1_form.addWidget(label)
w1_form.addWidget(line)
w1.setLayout(w1_form)

#tab2
w2 = QWidget()
b1 = QPushButton('btn1')
b2 = QPushButton('btn1')
b3 = QPushButton('btn1')
w2_layout = QVBoxLayout()
w2_layout.addWidget(b1)
w2_layout.addWidget(b2)
w2_layout.addWidget(b3)
w2.setLayout(w2_layout)

tab_w.addTab(w1, 'Tab1')
tab_w.addTab(w2, 'Tab2')

layout = QVBoxLayout()
layout.addWidget(tab_w)

window.setLayout(layout)
window.show()
app.exec()