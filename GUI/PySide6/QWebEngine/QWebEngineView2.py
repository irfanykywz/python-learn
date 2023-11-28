# https://doc.qt.io/qtforpython-6/overviews/qtwebenginewidgets-qtwebkitportingguide.html
# https://stackoverflow.com/questions/72781730/how-can-i-setting-the-user-agent-when-in-pyside6-webengineview
import sys

from PySide6.QtWidgets import *
from PySide6.QtWebEngineWidgets import QWebEngineView

def viewhtml(html):
    app = QApplication([])

    view = QWebEngineView()
    view.setHtml(html)
    view.show()

    app.exec_()
    
def viewurl(url):
    app = QApplication([])

    view = QWebEngineView()
    view.load(url)
    view.show()

    app.exec_()

viewurl('''https://doc.qt.io/qtforpython-6/overviews/qtwebenginewidgets-qtwebkitportingguide.html''')