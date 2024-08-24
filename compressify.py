import sys
import os
import ffmpeg
from PySide6 import QtCore, QtWidgets

from PySide6.QtWidgets import QPushButton, QFileDialog, QMessageBox


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Convert")
        self.text = QtWidgets.QLabel("Click the convert button to convert your file",
                                     alignment=QtCore.Qt.AlignCenter)
        self.encoder = "x265"
        #For NVIDIA GPUs
        self.nvencButton = QPushButton("NVENC (NVIDIA)", self)
        self.nvencButton.setFixedSize(120, 30)

        #For AMD GPUs
        self.AMFButton = QPushButton("AMF (AMD)", self)
        self.AMFButton.setFixedSize(120, 30)

        #For Intel iGPUs and Arc GPUs (to be tested)
        self.QuickSyncButton = QPushButton("QuickSync (Intel)", self)
        self.QuickSyncButton.setFixedSize(120, 30)

        self.x265Button = QPushButton("Software (CPU)", self)
        self.x265Button.setFixedSize(120, 30)


        self.setWindowTitle("Compressify")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

        self.layout.addWidget(self.nvencButton, alignment=QtCore.Qt.AlignBottom)
        self.layout.addWidget(self.AMFButton)
        self.layout.addWidget(self.QuickSyncButton)
        self.layout.addWidget(self.x265Button)
        self.layout.addWidget(self.button)


        self.button.clicked.connect(self.magic)
        self.x265Button.clicked.connect(self.x265clicked)
        self.nvencButton.clicked.connect(self.nvencClicked)
        self.AMFButton.clicked.connect(self.AMFClicked)
        self.QuickSyncButton.clicked.connect(self.quicksyncClicked)

    def x265clicked(self):
        self.encoder = "libx265"
        print(self.encoder)

    def nvencClicked(self):
        self.encoder = "hevc_nvenc"
        print(self.encoder)

    def AMFClicked(self):
        self.encoder = "hevc_amf"
        print(self.encoder)

    def quicksyncClicked(self):
        self.encoder = "hevc_qsv"
        print(self.encoder)



    @QtCore.Slot()
    def magic(self):
        # Open file dialog to select a file
        file_path = QFileDialog.getOpenFileName(self, "Choose File")
        if isinstance(file_path, tuple):
            file_path = file_path[0]
        if file_path:
            reply = QMessageBox.question(widget, 'Compress File',
                                         f"Do you want to compress {file_path}?",
                                         QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                         QMessageBox.StandardButton.No)
            #answer = mb.askquestion(title="Confirm?", message=fullmsg)

            if reply == QMessageBox.StandardButton.Yes:
                # Split the file path into directory, base filename, and extension
                # Split the file path into directory, base filename, and extension
                directory, filename = os.path.split(file_path)
                base_name, extension = os.path.splitext(filename)

                # Add "_compressed" to the filename
                outputfile = os.path.join(directory, f"{base_name}_compressed{extension}")

                # Print the original and new file paths
                print("Original file:", file_path)
                print("Output file:", outputfile)
                try:
                    (
                        ffmpeg
                        .input(file_path)
                        .output(outputfile, vcodec=self.encoder, crf=28)
                        .run()

                    )
                    print(f"File processed successfully: {outputfile}")
                    success = QMessageBox()
                    success.setText("File Compressed Successfuly!")
                    success.exec()
                except ffmpeg.Error as e:
                    print(f"An error occurred: {e.stderr.decode()}")
                    failure = QMessageBox()
                    failure.setText("Failed to compress file")
                    failure.exec()




if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())