# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox


class ButtonHolder(QWidget):
    def __init__(self):
        super().__init__()


        button = QPushButton("Klik 1")
        button.clicked.connect(self.buttonAct)

        layout = QVBoxLayout()
        layout.addWidget(button)
        # layout.addWidget(button2)
        self.setLayout(layout)



    def buttonAct(self):
        ret = QMessageBox.warning(self, "My Application",
        "The document has been modified.\n"
           "Do you want to save your changes?",
        QMessageBox.Save | QMessageBox.Discard
        | QMessageBox.Cancel,
        QMessageBox.Save)



app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()

# note
# error gak tau knp, padahal kodenya dari dokumentasinya langsung
# TypeError: 'PySide6.QtWidgets.QMessageBox.warning' called with wrong argument types:
# ternyata harus dipanggil lewat class ;3