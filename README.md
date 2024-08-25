# What is Compressify?
Compressify is a free and open source application made in Python to compress your audio/videos.

Report issues [here](https://github.com/Zyrnixx/Compressify/issues)

Feel free to contribute to this project to make Compressify even better!

![screenshot](https://raw.githubusercontent.com/Zyrnixx/Compressify/main/screenshot.png?token=GHSAT0AAAAAACURD5IVDR5OGQOBLM7IJV22ZWKMUNA)
# Usage
1. Open the software
2. Choose an encoder (AMF for AMD GPUs, NVENC for Nvidia GPUs, Quicksync for Intel GPUs, Software (x265) for CPUs)
3. Choose a file to compress

# What witchcraft is being done here?!
Compressify uses the [FFmpeg](https://ffmpeg.org/) project to convert videos that are encoded with [h264](https://en.wikipedia.org/wiki/Advanced_Video_Coding) into the more efficient [HEVC](https://en.wikipedia.org/wiki/High_Efficiency_Video_Coding) format. This decreases the file size considerably, and is very useful for large videos. Compatibility issues may arise with video players that do not have direct support for HEVC playback.

# Building from source
1. Clone the repo by running "git clone --recursive https://github.com/Zyrnixx/Compressify.git"
2. cd into the root of the project "cd Compressify"
3. Create a venv by running "python -m venv venv"
4. Install the requirements by running "pip install -r requirements.txt"
5. Run "pyinstaller compressify.py"

# TODO
* Test NVIDIA GPUs
* Test macOS on Intel and Apple Silicon
* Release on macOS
* Test Intel GPUs


Credits:

[Python](https://www.python.org/)

[PyQt6](https://pypi.org/project/PySide6/)

[ffmpeg-python](https://pypi.org/project/ffmpeg-python/)

[FFmpeg](https://ffmpeg.org/)

[PyInstaller](https://pypi.org/project/pyinstaller/)
