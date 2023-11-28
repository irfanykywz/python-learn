# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QComboBox, QPushButton, QVBoxLayout

def bu1do():
    print(f'item {co.currentText()} \n index {co.currentIndex()}')
def bu2do():
    co.setCurrentIndex(2)
def bu3do():
    for i in range(co.count()):
        print(f'index {i} : {co.itemText(i)}')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

co = QComboBox()
co.addItem('Eaw')
co.addItems(['Asu','Bagong'])

bu1 = QPushButton('current')
bu1.clicked.connect(bu1do)
bu2 = QPushButton('set')
bu2.clicked.connect(bu2do)
bu3 = QPushButton('get')
bu3.clicked.connect(bu3do)

vl = QVBoxLayout()
vl.addWidget(co)
vl.addWidget(bu1)
vl.addWidget(bu2)
vl.addWidget(bu3)
vl.addSpacing(100)

window.setLayout(vl)
window.show()
app.exec()