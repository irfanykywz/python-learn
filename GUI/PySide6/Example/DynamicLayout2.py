# https://python-forum.io/thread-31937-post-134868.html?highlight=PySide6#pid134868
import sys
import PySide6.QtWidgets as QtWidgets
  
class Test(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QVBoxLayout()
        self.btn1 = QtWidgets.QPushButton("HLayout")
        self.btn1.clicked.connect(self.setLayoutH)
        self.btn2 = QtWidgets.QPushButton("GLayout")
        self.btn2.clicked.connect(self.setLayoutG)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        w = QtWidgets.QWidget()
        w.setLayout(self.layout)
        self.setCentralWidget(w)
         
 
    def setLayoutG(self):        
        # gridlayout
        gridlayout = QtWidgets.QGridLayout()
        btn1 = QtWidgets.QPushButton("HLayout")
        gridlayout.addWidget(btn1)
        btn1.clicked.connect(self.setLayoutH)
        self.cwg = QtWidgets.QWidget()
        self.cwg.setLayout(gridlayout)        
        self.setCentralWidget(self.cwg)
         
    def setLayoutH(self):
        # hlayout
        hlayout = QtWidgets.QHBoxLayout()
        btn2 = QtWidgets.QPushButton("GLayout")
        btn2.clicked.connect(self.setLayoutG)
        hlayout.addWidget(btn2)
        self.editor = QtWidgets.QTextEdit()
        hlayout.addWidget(self.editor)
        self.cwh = QtWidgets.QWidget()
        self.cwh.setLayout(hlayout)
        self.setCentralWidget(self.cwh)
 
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = Test()
    win.setGeometry(0, 0, 400, 200)
    win.setWindowTitle("MyApp" + "[*]")
    win.show()
    sys.exit(app.exec_())