# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QSizePolicy, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

button1 = QPushButton('button1')
button2 = QPushButton('button2')
button3 = QPushButton('button3')
button3.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
button4 = QPushButton('button4')
button5 = QPushButton('button5')
button6 = QPushButton('button6')
button7 = QPushButton('button7')

grid = QGridLayout()
grid.addWidget(button1,0,0)
grid.addWidget(button2,0,1,1,2)
grid.addWidget(button3,1,0,2,1)
grid.addWidget(button4,1,1)
grid.addWidget(button5,1,2)
grid.addWidget(button6,2,1)
grid.addWidget(button7,2,2)

window.setLayout(grid)
window.show()
app.exec()