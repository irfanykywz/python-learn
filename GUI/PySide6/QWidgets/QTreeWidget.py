import sys
from PySide6.QtWidgets import QApplication, QTreeWidget, QTreeWidgetItem

app = QApplication(sys.argv)

data = {
    "Folder1": ['1','2','3','4'],
    "Folder2": ['a','b','c','d'],
    "Folder3": []
}

tree = QTreeWidget()
tree.setWindowTitle("pyside learn")
tree.setColumnCount(2)
tree.setHeaderLabels(['Folder','Action'])


items = []
for key, values in data.items():
    item = QTreeWidgetItem([key])
    for value in values:
        ext = value.split('.')[-1].upper()
        child = QTreeWidgetItem([value, ext])
        item.addChild(child)
    items.append(item)
tree.insertTopLevelItems(0, items)
tree.show()

app.exec()