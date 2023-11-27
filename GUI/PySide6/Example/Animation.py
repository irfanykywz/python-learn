# coding:utf-8
"""
Pyside Animation Script
Requirement:
PySide/examples/painting/concentriccircles.py
"""

import sys
from PySide6 import QtCore, QtGui, QtWidgets


class CircleWidget(QtWidgets.QWidget):
    """サークルを表示するクラス"""

    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)

        self.floatBased = False
        self.antialiased = False
        self.frameNo = 0

        self.setBackgroundRole(QtGui.QPalette.Base)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)

    def setFloatBased(self, floatBased):
        self.floatBased = floatBased
        self.update()

    def setAntialiased(self, antialiased):
        self.antialiased = antialiased
        self.update()

    def minimumSizeHint(self):
        """最小サイズ値の定義"""
        return QtCore.QSize(50, 50)

    def sizeHint(self):
        """規定サイズ値の定義"""
        return QtCore.QSize(180, 180)

    def nextAnimationFrame(self):
        """frame数をインクリメントして時間を進行させる"""
        self.frameNo += 1
        self.update()

    def paintEvent(self, event):
        # QPainterの生成
        painter = QtGui.QPainter()
        # QPainerの描画設定開始
        painter.begin(self)
        # レンダリング時にアンチエイリアスの指定
        painter.setRenderHint(QtGui.QPainter.Antialiasing, self.antialiased)
        # 拡大縮小?
        painter.translate(self.width() / 2, self.height() / 2)

        for diameter in range(0, 256, 30):
            # 半径の指定
            delta = abs((self.frameNo % 128) - diameter / 2)
            # 透過の指定
            alpha = 255 - (delta * delta) / 4 - diameter
            if alpha > 0:
                # ペンの色を指定
                painter.setPen(QtGui.QPen(QtGui.QColor(0, diameter /2, 127, alpha), 3))
                if self.floatBased:
                    # 座標値をfloatで指定
                    painter.drawEllipse(QtCore.QRectF(-diameter / 2.0, -diameter / 2.0, diameter, diameter))
                else:
                    # 座標値をintで指定
                    painter.drawEllipse(QtCore.QRect(-diameter / 2.0, -diameter / 2.0, diameter, diameter))
        painter.end()


class Window(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.aliasedLabel = self.createLabel(self.tr("Aliased"))
        self.antialiasedLabel = self.createLabel(self.tr("Antialiased"))
        self.intLabel = self.createLabel((self.tr("Int")))
        self.floatLabel = self.createLabel(self.tr("Float"))

        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.aliasedLabel, 0, 1)
        layout.addWidget(self.antialiasedLabel, 0, 2)
        layout.addWidget(self.intLabel, 1, 0)
        layout.addWidget(self.floatLabel, 2, 0)

        timer = QtCore.QTimer(self)

        self.circleWidgets = []
        for i in range(2):
            self.circleWidgets.append([None]*2)
            for j in range(2):
                self.circleWidgets[i][j] = CircleWidget()
                self.circleWidgets[i][j].setAntialiased(j != 0)
                self.circleWidgets[i][j].setFloatBased(i != 0)
                # timerオブジェクトのtimeアウトハンドルに、CircleWidgetのnextAnimationFrameをこねくと
                # 一定時間毎にアニメーションが更新される
                self.connect(timer, QtCore.SIGNAL("timeout()"), self.circleWidgets[i][j].nextAnimationFrame)

                layout.addWidget(self.circleWidgets[i][j], i+1, j+1)

        timer.start(10)
        self.setLayout(layout)

        self.setWindowTitle(self.tr("Concentric Circles"))


    def createLabel(selfself, text):
        label = QtWidgets.QLabel(text)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setMargin(2)
        label.setFrameStyle(QtWidgets.QFrame.Box | QtWidgets.QFrame.Sunken)
        return label

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())