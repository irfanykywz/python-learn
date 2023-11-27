from PySide6 import QtWidgets, QtGui, QtCore
# or from PySide2 import QtWidgets, QtGui, QtCore
import sys

class MovieSplashScreen(QtWidgets.QSplashScreen):

    def __init__(self, pathToGIF):
        self.movie = QtGui.QMovie(pathToGIF)
        self.movie.jumpToFrame(0)
        pixmap = QtGui.QPixmap(self.movie.frameRect().size())
        QtWidgets.QSplashScreen.__init__(self, pixmap, QtCore.Qt.WindowStaysOnTopHint)
        self.movie.frameChanged.connect(self.repaint)

    def showEvent(self, event):
        self.movie.start()

    def hideEvent(self, event):
        self.movie.stop()

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        pixmap = self.movie.currentPixmap()
        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap)


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self, None)
        self.setCentralWidget(QtWidgets.QLabel("Hello world!"))

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    pathToGIF = "./loading.gif"
    splash = MovieSplashScreen(pathToGIF)
    splash.show()

    def showWindow():
        splash.close()
        form.show()

    QtCore.QTimer.singleShot(3500, showWindow)
    form = MainWindow()
    app.exec_()