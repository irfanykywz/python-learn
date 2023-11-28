# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtWidgets import QApplication, QWidget, QGroupBox, QButtonGroup, QCheckBox, QRadioButton, QVBoxLayout

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")

mode = QGroupBox('mode')
rich = QCheckBox('rich')
young = QCheckBox('young')
smart = QCheckBox('smart')

mode_layout = QVBoxLayout()
mode_layout.addWidget(rich)
mode_layout.addWidget(young)
mode_layout.addWidget(smart)
mode.setLayout(mode_layout)

car = QGroupBox('you car')
ferari = QCheckBox('ferari')
lambo = QCheckBox('lambo')
nissan = QCheckBox('nissan')
bmw = QCheckBox('bmw')

car_button = QButtonGroup()
car_button.addButton(ferari)
car_button.addButton(lambo)
car_button.addButton(nissan)
car_button.addButton(bmw)
car_button.setExclusive(True)

car_layout = QVBoxLayout()
car_layout.addWidget(ferari)
car_layout.addWidget(lambo)
car_layout.addWidget(nissan)
car_layout.addWidget(bmw)
car.setLayout(car_layout)

active = QGroupBox('want to rich ?')
active_yes = QRadioButton('yes')
active_no = QRadioButton('no')
active_yes.setChecked(True)

active_layout = QVBoxLayout()
active_layout.addWidget(active_yes)
active_layout.addWidget(active_no)
active.setLayout(active_layout)

all_widget = QVBoxLayout()
all_widget.addWidget(mode)
all_widget.addWidget(car)
all_widget.addWidget(active)


window.setLayout(all_widget)
window.show()
app.exec()