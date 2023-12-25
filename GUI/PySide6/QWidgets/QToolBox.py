import sys
from PySide6.QtWidgets import QApplication, QToolBox, QMainWindow, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('QToolBox Example')

        toolbox = QToolBox()
        # toolbox.setStyleSheet('QToolBox::tab { width: 100px; }')

        for i in range(1, 4):
            widget = QWidget()
            layout = QVBoxLayout()

            button = QPushButton(f'Button {i}')
            layout.addWidget(button)

            widget.setLayout(layout)
            toolbox.addItem(widget, f'Tab {i}')

        self.setCentralWidget(toolbox)

app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())