import sys, os
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon

# set dir dynamic for icon
basedir = os.path.dirname(__file__)

app = QApplication(sys.argv)
# set app icon with QIcon
app.setWindowIcon(QIcon(os.path.join(basedir, 'icon.ico')))

window = QMainWindow()
window.setWindowTitle("pyside6 learn")
window.show()

app.exec()