import sys
from PySide6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem
from PySide6.QtGui import QColor

app = QApplication(sys.argv)


colors = [
    ['red', '#FF0000'],
    ['green', '#00FF00'],
    ['blue', '#0000FF']
]

def get_rgb_from_hex(code):
    code_hex = code.replace("#", "")
    rgb = tuple(int(code_hex[i:i+2],16) for i in (0,2,4))
    return QColor.fromRgb(rgb[0],rgb[1],rgb[2])

table = QTableWidget()
table.setRowCount(len(colors))
table.setColumnCount(len(colors[0]) + 1)
table.setHorizontalHeaderLabels(['Name','Hex','Color'])

for i, (name, code) in enumerate(colors):
    name = QTableWidgetItem(name)
    codew = QTableWidgetItem(code)
    color = QTableWidgetItem()
    color.setBackground(get_rgb_from_hex(code))

    table.setItem(i,0,name)
    table.setItem(i,1,codew)
    table.setItem(i,2,color)

table.show()

app.exec()