# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

def buttonSubmit():
    labelr.setText(f'Result : {line.text()}')
def lineChanged():
    pass
def cursorChanged():
    pass
def editingFinish():
    labelr.setText(f'Finish : {line.text()}')
def returnedPress():
    pass
def textEdited(val):
    print(val)


app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("pyside6 learn")

label = QLabel('Nama :')
line = QLineEdit()
line.textChanged.connect(lineChanged)
line.cursorPositionChanged.connect(cursorChanged)
line.editingFinished.connect(editingFinish)
line.returnPressed.connect(returnedPress)
line.textEdited.connect(textEdited)

h_layout = QHBoxLayout()
h_layout.addWidget(label)
h_layout.addWidget(line)

button = QPushButton('Register')
button.clicked.connect(buttonSubmit)
labelr = QLabel('Result')

v_layout = QVBoxLayout()
v_layout.addLayout(h_layout)
v_layout.addWidget(button)
v_layout.addWidget(labelr)
window.setLayout(v_layout)

window.show()
app.exec()