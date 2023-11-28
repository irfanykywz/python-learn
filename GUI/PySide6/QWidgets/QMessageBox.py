# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox

def buttonAct():
    m = QMessageBox()
    m.setMinimumSize(300,200)
    m.setWindowTitle('Alat untuk jadi anime')
    m.setText('kamu berhasil menjadi anime ?')
    m.setInformativeText('****************')
    # m.setIcon(QMessageBox.Critical)
    # m.setIcon(QMessageBox.Question)
    m.setIcon(QMessageBox.Information)
    # m.setIcon(QMessageBox.Warning)
    m.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    m.setDefaultButton(QMessageBox.Ok)
    ret = m.exec()
    if ret == QMessageBox.Ok:
        print('ok')
    else:
        print('cancel')



app = QApplication(sys.argv)
window = QWidget()

button = QPushButton("Klik 1")
button.clicked.connect(buttonAct)

layout = QVBoxLayout()
layout.addWidget(button)
# layout.addWidget(button2)
window.setLayout(layout)


window.show()
app.exec()