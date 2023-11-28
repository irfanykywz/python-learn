from PySide6 import QtCore, QtWidgets

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.handleTimeout)
        self.buttonStart = QtWidgets.QPushButton('Start')
        self.buttonStart.clicked.connect(self.handleStart)
        self.buttonStop = QtWidgets.QPushButton('Stop')
        self.buttonStop.clicked.connect(self.timer.stop)
        self.min = QtWidgets.QSpinBox()
        self.min.setRange(0, 10)
        self.sec = QtWidgets.QSpinBox()
        self.sec.setRange(0, 59)
        self.lcd = QtWidgets.QLCDNumber()
        layout = QtWidgets.QGridLayout(self)
        layout.addWidget(self.lcd, 0, 0, 1, 2)
        layout.addWidget(self.min, 1, 0)
        layout.addWidget(self.sec, 1, 1)
        layout.addWidget(self.buttonStart, 2, 0)
        layout.addWidget(self.buttonStop, 2, 1)
        self.time = QtCore.QTime(0, 0)
        self.handleTimeout()

    def handleStart(self):
        if not self.timer.isActive():
            self.time.setHMS(0, self.min.value(), self.sec.value())
            self.handleTimeout()
            self.timer.start()

    def handleTimeout(self):
        self.lcd.display(self.time.toString('m:ss'))
        if self.time.minute() or self.time.second():
            self.time = self.time.addSecs(-1)
        else:
            print('finish')
            self.timer.stop()

if __name__ == '__main__':

    app = QtWidgets.QApplication(['Test'])
    window = Window()
    window.setGeometry(600, 100, 300, 200)
    window.show()
    app.exec_()