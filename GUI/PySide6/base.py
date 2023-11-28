import sys
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")




window.show()
app.exec()