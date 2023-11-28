from PySide6 import QtWidgets,QtCore,QtGui
import sys, time
from PySide6.QtCore import Qt,QUrl
from PySide6 import QtWebEngineWidgets
from PySide6 import QtWebEngineCore

class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.centralwid=QtWidgets.QWidget(self)
        self.vlayout=QtWidgets.QVBoxLayout()
        self.webview=QtWebEngineWidgets.QWebEngineView()
        self.webview.setUrl(QUrl("https://www.youtube.com/watch?v=Mq4AbdNsFVw"))
        self.vlayout.addWidget(self.webview)
        self.centralwid.setLayout(self.vlayout)
        self.setCentralWidget(self.centralwid)
        self.show()

app=QtWidgets.QApplication([])
ex=window()
sys.exit(app.exec_())