import sys, requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")


img = QImage('QImage.png')

qout = QImage(img.size(), img.format())
qout.fill(Qt.transparent)
painter = QPainter(qout)
painter.setRenderHint(QPainter.Antialiasing, True);
painter.setRenderHint(QPainter.SmoothPixmapTransform, True);
path = QPainterPath()
radius = 400
r = qout.rect()
path.addRoundedRect(r.adjusted(0, 0, -0, -0), radius, radius)
path.closeSubpath()
painter.setClipPath(path)
painter.drawImage(QPoint(0, 0), img)
painter.end()

# qout.save("output.png")

label = QLabel()
label.setPixmap(QPixmap.fromImage(qout).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))

window.setCentralWidget(label)
window.show()
app.exec()