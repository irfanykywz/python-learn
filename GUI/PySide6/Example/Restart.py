# sys module for processing command line arguments
import sys, os, subprocess

# importing pyside6
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

FILEPATH = os.path.abspath(__file__)
print(FILEPATH)

def buttonClick(data):
    try:
        subprocess.Popen([sys.executable, FILEPATH])
    except OSError as exception:
        print('ERROR: could not restart aplication:')
        print('  %s' % str(exception))
    # else:
        # QApplication.quit()

app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("pyside6 learn")

button = QPushButton()
button.setText('Restart [PID: %d]' % QApplication.applicationPid())
button.setCheckable(True)
button.clicked.connect(buttonClick)

window.setCentralWidget(button)
window.show()

app.exec()