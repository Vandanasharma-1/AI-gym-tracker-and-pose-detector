
# AI Gym Tracker and Pose Detector

This project uses OpenCV and Mediapipe to count exercise repetitions, including bicep curls, squats, push-ups, and lunges. The script captures video from the webcam, processes it to detect specific poses, and counts repetitions based on the detected poses.

## Features

- **Bicep Curl Counter**
- **Squat Counter**
- **Push-up Counter**
- **Lunge Counter**

## Requirements

- Python 3.7+
- OpenCV
- Mediapipe
- NumPy
- PyInstaller

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Vandanasharma-1/AI-gym-tracker-and-pose-detector.git
    cd AI-gym-tracker-and-pose-detector
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

To run the exercise counter script, use the following command:
```sh
python app.py
 ```

The script will open your webcam feed and start detecting and counting the exercises.


## Building the Executable
To build the executable using PyInstaller, follow these steps:

1. Install PyInstaller:
```sh
pip install pyinstaller

```
2. Generate the spec file:
```sh
pyinstaller --name app --onefile --collect-data mediapipe app.py

 ```
3. Modify the generated app.spec file to include Mediapipe model files:
```sh
# app.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

from PyInstaller.utils.hooks import collect_data_files

mediapipe_data_files = collect_data_files('mediapipe')

a = Analysis(
    ['app.py'],
    pathex=['.'],
    binaries=[],
    datas=mediapipe_data_files,
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='app',
)


```
4. Build the executable:
```sh
pyinstaller app.spec

```
5. The executable will be created in the dist directory. Navigate to dist and run app.exe to test.

## Direct Execution

If you prefer not to install Python and dependencies, you can directly download and run the pre-built executable `app.exe` from this repository

1. Navigate to the [Releases](https://github.com/Vandanasharma-1/AI-gym-tracker-and-pose-detector/releases) section of this repository.
3. Downloaded the `app.exe` file.
4. Inside the extracted folder, locate the `app.exe` executable.
5. Run the `app.exe` executable.
6. The application will open, and you can start using it immediately without any additional setup.

Note: Ensure that your system meets the requirements specified in the README for the application to work properly.

## Contact Information

If you encounter any issues or have questions about using the application, feel free to contact me at [vandana.sharma727272@gmail.com](mailto:vandana.sharma727272@gmail.com). I'll be happy to assist you and provide a direct download link to the `app.exe` if needed.

## Notes
- Ensure that the webcam is connected and properly configured before running the script.
- You can adjust the detection confidence levels in the script by modifying the min_detection_confidence and min_tracking_confidence parameters when initializing the Mediapipe pose object.

## Troubleshooting
If you encounter a FileNotFoundError related to Mediapipe model files:

Make sure you included the Mediapipe model files in the datas parameter of the app.spec file.
Verify the Mediapipe model files are present in your Python environment's site-packages directory.

## Contributing
Feel free to open issues or submit pull requests if you have any improvements or bug fixes.


## Acknowledgements
- OpenCV - Open source computer vision and machine learning software library.

- MediaPipe - Cross-platform framework for building multimodal applied ML pipelines.