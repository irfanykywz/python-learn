# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QHBoxLayout, QVBoxLayout, QSizePolicy

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

label = QLabel('Label')
line = QLineEdit()
# line.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
line.setSizePolicy(QSizePolicy.Fixed,QSizePolicy.Fixed)

h_layout_1 = QHBoxLayout()
h_layout_1.addWidget(label)
h_layout_1.addWidget(line)

button1 = QPushButton('Button1')
button2 = QPushButton('Button2')
button3 = QPushButton('Button3')

h_layout_2 = QHBoxLayout()
h_layout_2.addWidget(button1,2)
h_layout_2.addWidget(button2,1)
h_layout_2.addWidget(button3,1)

v_layout = QVBoxLayout()
v_layout.addLayout(h_layout_1)
v_layout.addLayout(h_layout_2)

window.setLayout(v_layout)
window.show()
app.exec()