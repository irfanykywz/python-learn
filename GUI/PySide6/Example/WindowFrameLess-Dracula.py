import sys
from PySide6.QtCore import QPoint, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QSizeGrip, QPushButton, QVBoxLayout, QHBoxLayout



class MainWindow(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)

		self.setMinimumSize(600,300)
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setStyleSheet("QMainWindow {border:0px}")
		self.gripSize = 16
		self.grips = []
		for i in range(4):
			grip = QSizeGrip(self)
			grip.resize(self.gripSize, self.gripSize)
			self.grips.append(grip)

		self.start = QPoint(0, 0)
		self.pressing = False

		# set layout
		main_layout = QVBoxLayout()
		main_layout.setSpacing(0)
		main_layout.setContentsMargins(0, 0, 0, 0)
		main_layout.setAlignment(Qt.AlignTop)
		main_layout.addLayout(self.frameLayout())

		# set cental widget
		centralWidget = QWidget()
		centralWidget.setLayout(main_layout)
		self.setCentralWidget(centralWidget)
		
	def frameLayout(self):

		self.minimizeButton = QPushButton('-')
		self.maximizeButton = QPushButton('+')
		self.closeButton = QPushButton('x')

		horizontal = QHBoxLayout()
		horizontal.setAlignment(Qt.AlignRight)
		horizontal.addWidget(self.minimizeButton, 0)
		horizontal.addWidget(self.maximizeButton, 0)
		horizontal.addWidget(self.closeButton, 0)

		# set signal
		self.frameSignal()

		return horizontal

	def frameSignal(self):

		def minimize():
			self.showMinimized()

		def maximize():
			if self.windowState() == Qt.WindowMaximized:
				self.showNormal()
			else:
				self.showMaximized()

		def close():
			self.close()

		self.minimizeButton.clicked.connect(minimize)
		self.maximizeButton.clicked.connect(maximize)
		self.closeButton.clicked.connect(close)


	def resizeEvent(self, event):
		QMainWindow.resizeEvent(self, event)
		rect = self.rect()
		# top left grip doesn't need to be moved...
		# top right
		self.grips[1].move(rect.right() - self.gripSize, 0)
		# bottom right
		self.grips[2].move(
		rect.right() - self.gripSize, rect.bottom() - self.gripSize)
		# bottom left
		self.grips[3].move(0, rect.bottom() - self.gripSize)

	def mouseMoveEvent(self, event):
		if self.pressing:	
			self.end = self.mapToGlobal(event.pos())
			self.movement = self.end-self.start
			self.setGeometry(self.mapToGlobal(self.movement).x(),
			self.mapToGlobal(self.movement).y(),
			self.width(),
			self.height())
			self.start = self.end

	def mouseReleaseEvent(self, QMouseEvent):
		self.pressing = False

	def mousePressEvent(self, event):
		self.start = self.mapToGlobal(event.pos())
		self.pressing = True



app = QApplication(sys.argv)
window = MainWindow()


window.show()
app.exec()