# https://pythonassets.com/posts/download-file-with-progress-bar-pyqt-pyside/#google_vignette

from urllib.request import urlopen

from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtWidgets import QProgressBar


class Downloader(QThread):

    # Signal for the window to establish the maximum value
    # of the progress bar.
    setTotalProgress = Signal(int)
    # Signal to increase the progress.
    setCurrentProgress = Signal(int)
    # Signal to be emitted when the file has been downloaded successfully.
    succeeded = Signal()

    def __init__(self, url, filename):
        super().__init__()
        self._url = url
        self._filename = filename

    def run(self):
        url = "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe"
        filename = "python-3.7.2.exe"
        readBytes = 0
        chunkSize = 1024
        # Open the URL address.
        with urlopen(url) as r:
            # Tell the window the amount of bytes to be downloaded.
            self.setTotalProgress.emit(int(r.info()["Content-Length"]))
            with open(filename, "ab") as f:
                while True:
                    # Read a piece of the file we are downloading.
                    chunk = r.read(chunkSize)
                    # If the result is `None`, that means data is not
                    # downloaded yet. Just keep waiting.
                    if chunk is None:
                        continue
                    # If the result is an empty `bytes` instance, then
                    # the file is complete.
                    elif chunk == b"":
                        break
                    # Write into the local file the downloaded chunk.
                    f.write(chunk)
                    readBytes += chunkSize
                    # Tell the window how many bytes we have received.
                    self.setCurrentProgress.emit(readBytes)
        # If this line is reached then no exception has ocurred in
        # the previous lines.
        self.succeeded.emit()


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Download with progress in PySide")
        self.resize(400, 300)
        self.label = QLabel("Press the button to start downloading.", self)
        self.label.setGeometry(20, 20, 200, 25)
        self.button = QPushButton("Start download", self)
        self.button.move(20, 60)
        self.button.pressed.connect(self.initDownload)
        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(20, 115, 300, 25)

    def initDownload(self):
        self.label.setText("Downloading file...")
        # Disable the button while the file is downloading.
        self.button.setEnabled(False)
        # Run the download in a new thread.
        self.downloader = Downloader(
            "https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe",
            "python-3.7.2.exe"
        )
        # Connect the signals which send information about the download
        # progress with the proper methods of the progress bar.
        self.downloader.setTotalProgress.connect(self.progressBar.setMaximum)
        self.downloader.setCurrentProgress.connect(self.progressBar.setValue)
        # Qt will invoke the `succeeded()` method when the file has been
        # downloaded successfully and `downloadFinished()` when the
        # child thread finishes.
        self.downloader.succeeded.connect(self.downloadSucceeded)
        self.downloader.finished.connect(self.downloadFinished)
        self.downloader.start()

    def downloadSucceeded(self):
        # Set the progress at 100%.
        self.progressBar.setValue(self.progressBar.maximum())
        self.label.setText("The file has been downloaded!")

    def downloadFinished(self):
        # Restore the button.
        self.button.setEnabled(True)
        # Delete the thread when no longer needed.
        del self.downloader


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()