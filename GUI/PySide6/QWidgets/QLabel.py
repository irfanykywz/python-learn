import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtCore import Qt

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("pyside learn")

label = QLabel('this is label')
label.setAlignment(Qt.AlignCenter)

window.setCentralWidget(label)
window.show()

app.exec()