# sys module for processing command line arguments
import sys

# importing pyside6
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("pyside6 learn")


funList = QListWidget()
funList.setSelectionMode(QAbstractItemView.MultiSelection)

itemN = QListWidgetItem('assu')
#Create widget
widget = QWidget()
widgetText =  QLabel("I love PyQt!")
widgetButton =  QPushButton("Push Me")
widgetLayout = QHBoxLayout()
widgetLayout.addWidget(widgetText)
widgetLayout.addWidget(widgetButton)
widgetLayout.addStretch()

widgetLayout.setSizeConstraint(QLayout.SetFixedSize)
widget.setLayout(widgetLayout)
itemN.setSizeHint(widget.sizeHint())

#Add widget to QListWidget funList
funList.addItem(itemN)
# funList.setItemWidget(itemN, widget)

vl = QVBoxLayout()
vl.addWidget(funList)

window.setLayout(vl)
window.show()
app.exec()