# https://gist.github.com/peace098beat/e4fd11124bc0f5aba56f
#! coding:utf-8
"""
a
Created by 0160929 on 2016/03/18 10:40
"""
from PySide6.QtNetwork import QNetworkProxy

__version__ = '0.2'
__app_name__ = 'Recomen'

import sys

from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import QUrl, Qt
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy




# QWidgetを継承してブラウザーを作成するクラス
class browserUI(QWidget):
    # 初期化関数
    def __init__(self, parent=None):
        # スーパークラス（QWidget）のインスタンスメソッドからparentを使いたいのでsuper関数を使う
        super(browserUI, self).__init__(parent)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 最善面表示
        # self.setWindowFlags(Qt.FramelessWindowHint) # window枠の非表示

        self.resize(600, 350)  # サイズ変更

        # タイトルの変更
        self.setWindowTitle(
            QApplication.translate("Widget", "%s %s" % (__app_name__, __version__), None))

        # 背景の描画をOFF
        self.setAttribute(Qt.WA_TranslucentBackground, True)

        # CSSのセット
        # self.setCSS()
        # showUIメソッドの呼び出し
        self.showUI()

    def showUI(self):
        # レイアウトの作成
        vbox = QVBoxLayout(self)

        # ブラウザの作成
        self.browser = QWebEngineView(self)

        # 動画観覧用にプラグインの許可
        # self.browser.settings().setAttribute(luginsEnabled, True)
        # self.browser.settings().setAttribute(QWebSettings.AutoLoadImages, True)
        # self.browser.settings().setAttribute(QWebSettings.JavascriptEnabled, True)


        # Enable plugin/javascript/storage
        # webSetting = QWebSettings.globalSettings()
        # webSetting.setAttribute(QWebSettings.PluginsEnabled, True)
        # webSetting.setAttribute(QWebSettings.DnsPrefetchEnabled, True)
        # webSetting.setAttribute(QWebSettings.JavascriptEnabled, True)
        # webSetting.setAttribute(QWebSettings.OfflineStorageDatabaseEnabled, True)
        # webSetting.setAttribute(QWebSettings.LocalStorageEnabled, True)


        # プロキシの設定
        # proxy = QNetworkProxy()
        # proxy.setType(QNetworkProxy.HttpProxy)
        # proxy.setType(QNetworkProxy.DefaultProxy)
        # proxy.setHostName("kwgproxya")
        # proxy.setPort(8080)
        # proxy.setUser("0160929")
        # proxy.setPassword("FFF2121098PBFFFpx12")
        # QNetworkProxy.setApplicationProxy(proxy)
        # self.browser.page().networkAccessManager().setProxy(proxy)

        # URLの設定
        # self.browser.load(QUrl('http://localhost/Recomen/www/strong-player.html'))
        # self.browser.load(QUrl('https://www.youtube.com/watch?v=BDOiHSZ9g0E'))
        self.browser.load(QUrl('https://www.google.co.jp/'))

        # レイアウトにアタッチ
        vbox.addWidget(self.browser)
        # 親レイアウトに合わせて伸縮する設定
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

    def setCSS(self):
        """
        同じフォルダにあるcssを読みこんでセット
        """
        with open("user-style.css", "r") as f:
            self.setStyleSheet("".join(f.readlines()))


def main():
    app = QApplication(sys.argv)
    app.setStyle('plastique')
    win = browserUI()
    win.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()