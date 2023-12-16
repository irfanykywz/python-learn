import subprocess
import time
import win32gui



def run_app():
    from PySide6.QtGui import QWindow
    from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton

    app = QApplication([])

    # create a process
    exePath = "C:\\Windows\\system32\\calc.exe"
    subprocess.Popen(exePath)
    time.sleep(5)
    hwnd = win32gui.FindWindowEx(0, 0, "CalcFrame", "Calc")
    print(hwnd)
    window = QWindow.fromWinId(hwnd)
    widget = QWidget()
    widget.createWindowContainer(window, widget)
    widget.setGeometry(500, 500, 450, 400)
    widget.setWindowTitle('File dialog')
    widget.show()

    app.exec_()


if __name__ == '__main__':
   run_app()