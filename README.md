Compressify is a free and open source application made in Python to compress your audio/videos.

# Usage
1. Open the software
2. Choose an encoder (AMF for AMD GPUs, NVENC for Nvidia GPUs, Quicksync for Intel GPUs)
3. Choose a file to compress

# Building from source
1. Clone the repo by running "git clone --recursive https://github.com/Zyrnixx/Compressify.git" in a terminal/command prompt
2. cd into the root of the project by running "cd Compressify"
3. Create a venv by running "python -m venv venv"
4. Activate venv by running:
* Windows (Command Prompt): ".\venv\Scripts\activate.bat"
* Windows (Powershell): ".\venv\Scripts\Activate.ps1"
* macOS/Linux: "source venv/bin/activate"
5. Install the requirements by running "pip install -r requirements.txt"
6. Run "pyinstaller main.py"


Credits:

[Python](https://www.python.org/)

[PyQt6](https://pypi.org/project/PySide6/)

[ffmpeg-python](https://pypi.org/project/ffmpeg-python/)

[FFmpeg](https://ffmpeg.org/)

[PyInstaller](https://pypi.org/project/pyinstaller/)
