import sys, requests
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel

app = QApplication(sys.argv)
window = QMainWindow()
window.setWindowTitle("pyside learn")


url = 'https://scontent-cgk1-2.xx.fbcdn.net/v/t39.30808-6/379532438_1770029780088226_2143147894079240259_n.jpg?_nc_cat=107&ccb=1-7&_nc_sid=a2f6c7&_nc_ohc=sENnidXxPz8AX_DVYc5&_nc_ht=scontent-cgk1-2.xx&oh=00_AfCJd-J3cRaFS4gm-kq2QHRugForEsJDnMuTQKn5OZmPbw&oe=6526D354'
r = requests.get(url)
print(r.content)
img = QImage()
img.loadFromData(r.content)

label = QLabel()
label.setPixmap(QPixmap.fromImage(img).scaled(300, 300, Qt.AspectRatioMode.KeepAspectRatio))
# label.setPixmap(QPixmap.fromImage(img).scaled(80, 80, Qt.AspectRatioMode.IgnoreAspectRatio))

window.setCentralWidget(label)
window.show()
app.exec()