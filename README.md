Compressify is a free and open source application made in Python to compress your audio/videos.

Report issues [here](https://github.com/Zyrnixx/Compressify/issues)

Feel free to contribute to this project to make Compressify even better!

# Usage
1. Open the software
2. Choose an encoder (AMF for AMD GPUs, NVENC for Nvidia GPUs, Quicksync for Intel GPUs)
3. Choose a file to compress

# Building from source
1. Clone the repo by typing "git clone --recursive https://github.com/Zyrnixx/Compressify.git"
2. cd into the root of the project "cd Compressify"
3. create a venv by running "python -m venv venv"
4. install the requirements by typing "pip install -r requirements.txt"
5. run "pyinstaller main.py"

# TODO
* Test NVIDIA GPUs
* Test macOS on Intel and Apple Silicon (M1 and up)
* Test Intel GPUs


Credits:

[Python](https://www.python.org/)

[PyQt6](https://pypi.org/project/PySide6/)

[ffmpeg-python](https://pypi.org/project/ffmpeg-python/)

[FFmpeg](https://ffmpeg.org/)

[PyInstaller](https://pypi.org/project/pyinstaller/)
