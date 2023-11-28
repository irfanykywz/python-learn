# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

def buttonClick(data):
    print('checked :', data)
def buttonPress():
    print('press')
def buttonRess():
    print('ress')

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("pyside6 learn")

button = QPushButton()
button.setText('Press Me')
button.setCheckable(True)
button.clicked.connect(buttonClick)
button.pressed.connect(buttonPress)
button.released.connect(buttonRess)

window.setCentralWidget(button)
window.show()

app.exec()