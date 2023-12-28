import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTabWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # Create QTabWidget and QVBoxLayout
        self.tabWidget = QTabWidget()
        self.setCentralWidget(self.tabWidget)

        # Create QPushButton and QVBoxLayout
        self.addButton = QPushButton('Add Tab')
        self.addButton.clicked.connect(self.addTab)
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)

        # Create QWidget, set layout, and add it to the QTabWidget
        container = QWidget()
        container.setLayout(layout)
        self.tabWidget.addTab(container, '+')

        self.setWindowTitle('QTabWidget Example')
        self.setGeometry(300, 300, 400, 200)

    def addTab(self):
        # Create QWidget, QVBoxLayout, and QPushButton
        newTab = QWidget()
        layout = QVBoxLayout()
        label = QPushButton('New Tab')

        # Add QPushButton to QVBoxLayout and set QVBoxLayout to QWidget
        layout.addWidget(label)
        newTab.setLayout(layout)

        # Add QWidget to QTabWidget
        self.tabWidget.insertTab(self.tabWidget.count() - 1, newTab, 'Tab')

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec())