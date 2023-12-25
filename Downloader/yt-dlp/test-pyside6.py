import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PySide6.QtCore import QObject, QThread, Signal
import yt_dlp

class Worker(QObject):
    finished = Signal()
    error = Signal(str)

    def __init__(self, url):
        super().__init__()
        self.url = url

    def run(self):
        try:
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([self.url])
        except Exception as e:
            self.error.emit(str(e))
        finally:
            self.finished.emit()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('YT-DL Pythin-Qt Side')
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()

        self.label = QLabel('Enter Youtube URL:')
        self.layout.addWidget(self.label)

        self.line_edit = QLineEdit()
        self.layout.addWidget(self.line_edit)

        self.button = QPushButton('Download')
        self.button.clicked.connect(self.start_download)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def start_download(self):
        url = self.line_edit.text()
        if not url:
            return

        self.thread = QThread()
        self.worker = Worker(url)
        self.worker.moveToThread(self.thread)

        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.error.connect(self.display_error)

        self.button.setEnabled(False)
        self.thread.start()

    def display_error(self, error):
        print(error)
        self.button.setEnabled(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())