import sys
import os
from tkinter import messagebox as mb
import ffmpeg
from PySide6 import QtCore, QtWidgets
from tkinter import filedialog

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.button = QtWidgets.QPushButton("Convert")
        self.text = QtWidgets.QLabel("Click the convert button to convert your video",
                                     alignment=QtCore.Qt.AlignCenter)
        self.fileSTR = QtWidgets.QLabel("N/A",
                                        alignment=QtCore.Qt.AlignBottom)
        self.setWindowTitle("Compressify")
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.fileSTR)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        # Open file dialog to select a file
        file_path = filedialog.askopenfilename()

        if file_path:
            msg = "are you sure you want to compress the file:"
            msgp2 = "?"
            fullmsg = (msg, file_path, msgp2)
            self.fileSTR.setText(file_path)
            answer = mb.askquestion(title="Confirm?", message=fullmsg)

            if answer == "yes":
                # Split the file path into directory, base filename, and extension
                directory, filename = os.path.split(file_path)
                base_name, extension = os.path.splitext(filename)

                # Add "_output" to the filename
                outputfile = os.path.join(directory, f"{base_name}_compressed{extension}")

                # Print the original and new file paths
                print("Original file:", file_path)
                print("Output file:", outputfile)
                try:
                    (
                        ffmpeg
                        .input(file_path)
                        .output(outputfile, vcodec='libx265', crf=28)
                        .run()

                    )
                    print(f"Video processed successfully: {outputfile}")
                    mb.showinfo(title="Success!", message="Your file has been compressed!")
                except ffmpeg.Error as e:
                    print(f"An error occurred: {e.stderr.decode()}")
                    mb.showerror(title="Error!", message="Your file could not be converted.")





if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()

    sys.exit(app.exec())