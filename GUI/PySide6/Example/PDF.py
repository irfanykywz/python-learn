# https://gist.github.com/Axel-Erfurt/e9b7cda9e4da355ad7905186d11a22bb
from PySide6.QtCore import QUrl
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtWebEngineWidgets import QWebEngineView #, QWebEngineSettings
from os import path

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("PDF Viewer")
        self.setGeometry(0, 28, 1000, 750)

        self.webView = QWebEngineView()
        self.webView.urlChanged.connect(self.url_changed)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PluginsEnabled, True)
        self.webView.settings().setAttribute(self.webView.settings().WebAttribute.PdfViewerEnabled, True)
        self.setCentralWidget(self.webView)

    def url_changed(self):
        self.setWindowTitle(self.webView.title())

    def go_back(self):
        self.webView.back()

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    if len(sys.argv) > 1:
        win.webView.load(QUrl(f"file://{sys.argv[1]}"))
    sys.exit(app.exec())