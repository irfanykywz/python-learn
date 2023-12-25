import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QTabBar, QStackedWidget
from PySide6.QtCore import Qt

class MultiRowTabWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.tab_bar = QTabBar()
        self.tab_bar.addTab('Tab 1')
        self.tab_bar.addTab('Tab 2')
        self.tab_bar.addTab('Tab 3')
        self.tab_bar.addTab('Tab 4')
        self.tab_bar.addTab('Tab 5')
        self.tab_bar.addTab('Tab 6')
        self.tab_bar.addTab('Tab 7')

        self.stacked_widget = QStackedWidget()
        # for i in range(4):
        #     widget = QWidget()
        #     layout = QGridLayout()

        #     button = QPushButton(f'Button {i + 1}')
        #     layout.addWidget(button)

        #     widget.setLayout(layout)
        #     self.stacked_widget.addWidget(widget)

        layout.addWidget(self.tab_bar, 0, 0, 1, 4)
        layout.addWidget(self.stacked_widget, 1, 0, 1, 4)

        # self.tab_bar.currentChanged.connect(self.stacked_widget.setCurrentIndex)

        self.setLayout(layout)

app = QApplication(sys.argv)
main_window = QMainWindow()
main_window.setCentralWidget(MultiRowTabWidget())
main_window.show()
sys.exit(app.exec())