import sys
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")


def signalButton():
    if button.isChecked():
        button.setText('Stop')
        print('has started')
    else:
        def asu():
            button.setEnabled(True)
            button.setText('Start')
        print('has stoped')
        button.setDisabled(True)
        # button.setText(QTimer.remainingTime())
        # before start again we need timer
        QTimer.singleShot(4000, asu)
        button.setText('stop process...')

button = QPushButton('Start')
button.setCheckable(True)
button.clicked.connect(signalButton)

# def doing():
#     print('test')

# timer = QTimer()
# # timer.singleShot(False)
# timer.timeout.connect(doing)
# timer.start(1000)

# QTimer.singleShot(4000, lambda: self._startBtn.setEnable)




window.setCentralWidget(button)

window.show()
app.exec()