import sys
from PySide6 import QtWidgets, QtCore
 
 
def new_timer(description: str, hour: int, minutes: int) -> QtWidgets.QWidget:
 
    def remove_timer(layout: QtWidgets.QLayout, widget: QtWidgets.QWidget) -> None:
        layout.removeWidget(widget)
        widget.deleteLater()
 
    widget = QtWidgets.QWidget()
    layout = QtWidgets.QGridLayout(widget)
 
    label = QtWidgets.QLabel(description)
    edit_timer = QtWidgets.QTimeEdit(time=QtCore.QTime(hour, minutes))
    btn_remove = QtWidgets.QPushButton(text="Remove Timer")
    btn_remove.clicked.connect(lambda: remove_timer(layout, widget))
 
    layout.addWidget(label, 0, 0)
    layout.addWidget(edit_timer, 1, 0)
    layout.addWidget(btn_remove, 2, 0)
 
    return widget
 
 
class TimerWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
  
        self.grid = QtWidgets.QGridLayout()
        self.grid.setSpacing(10)
        self.widget = QtWidgets.QWidget()
        self.layout = QtWidgets.QGridLayout(self.widget)
  
        # Mockup data
        self.timers = [
            new_timer("Alarme 1", 9, 15),
            new_timer("Alarme 2", 4, 15),
            new_timer("Alarme 3", 16, 20)
        ]
        for i, timer in enumerate(self.timers):
            self.layout.addWidget(timer, i, 0)
  
        self.scroll = QtWidgets.QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setWidget(self.widget)
        self.setCentralWidget(self.scroll)   # Add scroll area widget to the main window.
 
 
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    dialog = TimerWindow()
    dialog.show()
    sys.exit(app.exec())