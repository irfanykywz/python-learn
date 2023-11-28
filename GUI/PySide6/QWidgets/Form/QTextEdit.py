# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QTextEdit, QHBoxLayout, QVBoxLayout, QLabel, QPushButton

def currentText():
    print(tedit.toPlainText())
def setText():
    tedit.setPlainText('asu')
def setHTML():
    tedit.setHtml('<p>hahaha</p><b>asssu</b><h1>hahaha</h1>')

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

tedit = QTextEdit()

buttonCurrent = QPushButton('Current Text')
buttonCurrent.clicked.connect(currentText)
buttonCopy = QPushButton('Copy')
buttonCopy.clicked.connect(tedit.copy)
buttonCut = QPushButton('Cut')
buttonCut.clicked.connect(tedit.cut)
buttonPaste = QPushButton('Paste')
buttonPaste.clicked.connect(tedit.paste)
buttonUndo = QPushButton('Undo')
buttonUndo.clicked.connect(tedit.undo)
buttonRedo = QPushButton('Redo')
buttonRedo.clicked.connect(tedit.redo)
buttonSetText = QPushButton('SetText')
buttonSetText.clicked.connect(setText)
buttonsetHTML = QPushButton('setHTML')
buttonsetHTML.clicked.connect(setHTML)
buttonClear = QPushButton('Clear')
buttonClear.clicked.connect(tedit.clear)

h_layout = QHBoxLayout()
h_layout.addWidget(buttonCurrent)
h_layout.addWidget(buttonCopy)
h_layout.addWidget(buttonCut)
h_layout.addWidget(buttonPaste)
h_layout.addWidget(buttonUndo)
h_layout.addWidget(buttonRedo)
h_layout.addWidget(buttonSetText)
h_layout.addWidget(buttonsetHTML)
h_layout.addWidget(buttonClear)

v_layout = QVBoxLayout()
v_layout.addLayout(h_layout)
v_layout.addWidget(tedit)
window.setLayout(v_layout)

window.show()
app.exec()