import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QSize


app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("pyside6 learn")
# can't fullscreen
# window.setFixedSize(QSize(400, 300))
# minimum
window.setMinimumSize(QSize(400, 300))
# maximum
# window.setMaximumSize(QSize(1200,1024))
window.show()

app.exec()