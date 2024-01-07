# https://stackoverflow.com/questions/57246033/how-to-restart-the-app-with-single-process
# https://forum.qt.io/topic/110418/how-to-destroy-a-singleton-and-then-create-a-new-one/11
import sys

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MainWindow(QMainWindow):
    EXIT_CODE_REBOOT = 122
    def __init__(self):
        super().__init__()
        self.restart_button = QPushButton('restart')
        self.restart_button.clicked.connect(self.onRestart)

        self.setCentralWidget(self.restart_button)

        self.systray = QSystemTrayIcon(self)
        icon = self.style().standardIcon(QStyle.SP_TrashIcon)
        self.systray.setIcon(icon)
        self.systray.show()

    def onRestart(self, checked):
        self.systray.deleteLater()
        QApplication.exit(self.EXIT_CODE_REBOOT)

if __name__ == '__main__':
    currentExitCode = MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        app = QApplication.instance()
        if app == None:
            app = QApplication(sys.argv)
        mainwindow = MainWindow()
        mainwindow.show()
        currentExitCode = app.exec()