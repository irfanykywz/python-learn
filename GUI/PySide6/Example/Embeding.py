# https://www.pythonguis.com/faq/pyqt5-embed-external-program-into-qwidget/
# https://forum.qt.io/topic/132721/opening-external-application-and-embed-it-without-opening-application-out-of-application
# https://www.google.com/search?q=embed+other+aplication+pyqt&oq=embed+other+aplication+pyqt&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIJCAEQIRgKGKAB0gEINTk1MWowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
 
from screeninfo import get_monitors
import win32gui, win32process, psutil, json

def get_args(pid):
    args = {}

    try:
        for d in psutil.Process(pid).cmdline():
            if '=' in d:
                dd = d.split('=')
                args[dd[0]] = dd[1]
    finally:
        return args

def chrome_list():
    result = []

    def enumHandler(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            txt = win32gui.GetWindowText(hwnd)
            pids = win32process.GetWindowThreadProcessId(hwnd)
            for pid in pids:
                args = get_args(pid)
                # if '--window-size' not in args:
                #     continue
                if '--remote-debugging-port' in args and txt:
                    lParam += [hwnd]
            # if 'Facebook' in win32gui.GetWindowText(hwnd):
            #     lParam += [hwnd]
    win32gui.EnumWindows(enumHandler, result)
    return result

def run_app(window_id):
    from PySide6.QtGui import QWindow
    from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton

    app = QApplication([])
    main_widget = QWidget()
    layout = QVBoxLayout(main_widget)

    for idx in window_id:
    	window = QWindow.fromWinId(idx)
    	widget = QWidget.createWindowContainer(window)
    	layout.addWidget(widget)

    button = QPushButton('Close')
    button.clicked.connect(main_widget.close)
    layout.addWidget(button)

    main_widget.show()
    app.exec_()


if __name__ == '__main__':
    window_id = chrome_list()
    print(window_id)
    if window_id:
        run_app(window_id)