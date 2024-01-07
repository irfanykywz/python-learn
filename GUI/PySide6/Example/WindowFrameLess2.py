# https://stackoverflow.com/questions/44241612/custom-titlebar-with-frame-in-pyqt5
import sys

from PySide6.QtCore import QPoint
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import QApplication, QHBoxLayout, QLabel, QPushButton, \
QVBoxLayout, QWidget, QStyle 

class MainWindow(QWidget):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.layout  = QVBoxLayout()
        #self.titleBar = MyBar(self)        
        self.layout.addWidget(MyBar(self))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addStretch(-1)
        self.setMinimumSize(800,400)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False
        self.setStyleSheet(stylesheet1(self))
        
class MyBar(QWidget):

    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(10) # to set spacing between buttons
        self.title = QLabel("My Beautifull Bar created by L.Lespes")
        self.title.setFixedHeight(37)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title) # First widget in the layout               
        btn_size = 40
        size = QSize(30, 30) # button icon size
        style = self.style()  # Get the QStyle object from the widget, e.g. usually `self`

        # List of builtin icons for titlebar buttons
        icons = [
            'SP_TitleBarMinButton',
            'SP_TitleBarNormalButton',
            'SP_TitleBarMaxButton',                       
            'SP_TitleBarCloseButton',
         ]
        # List of buttons 
        bouton = ['min', 'normal', 'max', 'close']
        
        # Now let's create the buttons.    
        for i,b in zip(icons, bouton):
                self.button = QPushButton()
                self.layout.addWidget(self.button)
                if b == 'min':                  
                   self.button.setIcon(style.standardIcon(getattr(QStyle, i)))
                   self.button.setFixedSize(btn_size,btn_size)
                   self.button.setIconSize(size) 
                   self.button.clicked.connect(self.btn_min_clicked)
                   self.button.setToolTip('Minimize')
                   setattr(self, b + 'Button', self.button) # To be able to address this particular button
                elif b == 'normal':
                   self.button.setIcon(style.standardIcon(getattr(QStyle, i)))        
                   self.button.clicked.connect(self.btn_normal_clicked)
                   self.button.setFixedSize(btn_size, btn_size)
                   self.button.setIconSize(size)
                   self.button.setToolTip('Normal Window')
                   setattr(self, b + 'Button', self.button) # To be able to address this particular button
                elif b == 'max':
                   self.button.setIcon(style.standardIcon(getattr(QStyle,i)))        
                   self.button.clicked.connect(self.btn_max_clicked)
                   self.button.setFixedSize(btn_size, btn_size)
                   self.button.setIconSize(size)
                   self.button.setToolTip('Maximize Window')
                   setattr(self, b + 'Button', self.button) # To be able to address this particular button
                elif b == 'close':
                   self.button.setIcon(style.standardIcon(getattr(QStyle, i))) # To paint the button with builtin icon represented by (i)
                   self.button.setFixedSize(btn_size,btn_size)
                   self.button.setIconSize(size)
                   self.button.setToolTip('Close Window')
                   self.button.clicked.connect(self.btn_close_clicked)                
                   self.button.setStyleSheet("""
                   QPushButton:hover {
                   background-color:#4fc3f7;
                   background: qradialgradient(cx: 0.3, cy: -0.4,
                   fx: 0.3, fy: -0.4,
                   radius: 1.35, stop: 0 #fff, stop: 1 red);
                   color: red;
                   }        
               """)                   

        self.setLayout(self.layout)                                        
        self.normalButton.hide()
        self.start = QPoint(0, 0)
        self.pressing = False         
                        
        self.title.setStyleSheet("""
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightgray, stop:1 black);
        font-size: 14pt;
        font: 20pt Comic Sans MS;
        color:yellow;
        border-radius: 8px;
        """)         
        
        self.setStyleSheet("""
        QPushButton {
        color:#4fc3f7;
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightgray, stop:1 white);
        border:2px solid #4fc3f7;
        font-size:40px;
        font-weight:bold;
}
        QPushButton:hover {
        background-color:#4fc3f7;
        background: qradialgradient(cx: 0.3, cy: -0.4,
        fx: 0.3, fy: -0.4,
        radius: 1.35, stop: 0 #fff, stop: 1 #bbb);
        color: white;
        }
        
        QPushButton:pressed {
        color:white;
        background-color:#212121;
        border-color:white;
        background: qradialgradient(cx: 0.4, cy: -0.1,
        fx: 0.4, fy: -0.1,
        radius: 1.35, stop: 0 #fff, stop: 1 #ddd);
        }
                       
        QPushButton::groove {
        border: 1px solid #bbb;
        background: lightgray;
        height: 10px;
        border-radius: 4px;
        }
                
                """)                

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.resize(self.minButton.x(), self.height())
        
    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end-self.start
            self.window().setGeometry(self.mapToGlobal(self.movement).x(),
                                self.mapToGlobal(self.movement).y(),
                                self.window().width(),
                                self.window().height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.window().close()
        
    def btn_max_clicked(self):
        if self.window().isMaximized():
            self.maxButton.show()
            self.normalButton.hide()
        else:
            self.window().showMaximized()
            self.maxButton.hide()
            self.normalButton.show()            
            
    def btn_min_clicked(self):
        self.window().showMinimized()
        
    def btn_normal_clicked(self):
        self.normalButton.hide()
        self.maxButton.show()
        self.window().showNormal()
             
 ###############################################################                                                
def stylesheet1(self):
    return """    
QWidget {
    selection-color: white;
    border: 3px solid  orange;
    /*border-style:none;*/
    selection-background-color: Silver;
    color: blue;
    /*background-color: #222222*/
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, 
        stop: 0 #cccccc, stop: 1 #333333);
}

/*A QFrame is styled using the The Box Model.*/

 QFrame{
     border: 2px solid green;
     border-radius: 4px;
     padding: 2px;
 }
 
QToolTip{
    background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #cccccc, stop: 1 #333333);
    color: white;
    font-size: 20px;
    border-radius: 8px;
    border-color: beige;
    border-top: 3px transparent;
    border-bottom: 3px transparent;
    border-right: 10px transparent;
    border-left: 10px transparent;         
    }
/*        
QLabel {
   background-color: #222222;
   color: yellow;
   font-size:18px;
   border-width: 1px;
   border-style:none;
   padding-top: 2px;
   padding-bottom: 2px;
   padding-left: 2px;
   padding-right: 2px;
}

QLabel {  
  background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 lightgray, stop:1 black);
  padding: 4px;
  font-size: 14pt;
  color:yellow;
  min-height: 30px; 
}
*/
    """               
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())