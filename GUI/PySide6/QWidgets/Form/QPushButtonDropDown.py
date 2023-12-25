# https://www.blackbox.ai/
# qpushbutton with qmenu pyside6
from PySide6.QtWidgets import QPushButton, QMenu, QVBoxLayout, QApplication, QWidget
import sys

class QDropdownButton(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # create QPushButton and QMenu
        self.push_button = QPushButton('Select')
        self.menu = QMenu()

        # add items to QMenu
        self.menu.addAction('Item 1')
        self.menu.addAction('Item 2')
        self.menu.addAction('Item 3')

        # set QMenu to QPushButton
        self.push_button.setMenu(self.menu)
        self.push_button.setStyleSheet("""
        QPushButton::menu-indicator { image: none; }
        """)

        # create QVBoxLayout and add widgets
        vbox = QVBoxLayout()
        vbox.addWidget(self.push_button)

        # set layout
        self.setLayout(vbox)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dropdown_button = QDropdownButton()
    dropdown_button.setGeometry(100, 100, 300, 100)
    dropdown_button.show()
    sys.exit(app.exec_())