# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QCheckBox, QListWidget, QAbstractItemView


def cItemChange(item):
    print(f'Current Item : {item.text()}')
def cTextChange(text):
    print(f'Current text : {text}')

def add():
    lwidget.addItem('new Item')
def delete():
    lwidget.takeItem(lwidget.currentRow())
def count():
    print(f'{lwidget.count()}')
def selected():
    list = lwidget.selectedItems()
    for i in list:
        print(i.text())

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

lwidget = QListWidget()
lwidget.setSelectionMode(QAbstractItemView.MultiSelection)
lwidget.addItem('one')
lwidget.addItems(['two','thre'])
lwidget.currentItemChanged.connect(cItemChange)
lwidget.currentTextChanged.connect(cTextChange)

button1 = QPushButton('Add')
button1.clicked.connect(add)
button2 = QPushButton('Delete')
button2.clicked.connect(delete)
button3 = QPushButton('Count')
button3.clicked.connect(count)
button4 = QPushButton('Selected')
button4.clicked.connect(selected)

vl = QVBoxLayout()
vl.addWidget(lwidget)
vl.addWidget(button1)
vl.addWidget(button2)
vl.addWidget(button3)
vl.addWidget(button4)

window.setLayout(vl)
window.show()
app.exec()