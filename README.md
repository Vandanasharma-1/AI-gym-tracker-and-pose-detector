AI Gym Tracker and Pose Detector

This project is an AI Fitness Tracker that uses OpenCV and MediaPipe to detect and count exercise repetitions in real-time using a webcam. The exercises supported include bicep curls, squats, push-ups, and lunges. The application is packaged as a standalone executable.

Table of Contents
Introduction
Features
Installation
Usage
Converting to Executable
Acknowledgments
License

Introduction
The Pose Exercise Counter utilizes OpenCV for capturing video frames and MediaPipe Pose for pose estimation. By calculating angles between key points on the body, it determines the stage of the exercise and counts the repetitions.

Features
Real-time Exercise Detection: Uses OpenCV and MediaPipe to detect body landmarks and calculate angles for exercise counting.
Exercise Counter: Automatically counts repetitions for bicep curls, squats, push-ups, and lunges.
Visual Feedback: Displays the live feed with detected landmarks and angles, along with the count of repetitions.

Installation
Prerequisites
Python 3.11
pip (Python package installer)
OpenCV
MediaPipe
NumPy
Clone the Repository

git clone https://github.com/yourusername/pose-exercise-counter.git
cd pose-exercise-counter
Install Dependencies

pip install -r requirements.txt
Requirements File (requirements.txt)
Copy code
opencv-python-headless
mediapipe
numpy
Usage
Run the following command to start the application:


python app.py
The application will open a webcam feed window. Perform bicep curls, squats, push-ups, or lunges in front of the camera, and the application will count your repetitions.

Keyboard Controls
Press q to quit the application.
Converting to Executable
To convert the Python script to an executable using PyInstaller:

Install PyInstaller:

pip install pyinstaller
Use PyInstaller to create the executable:

pyinstaller --onefile --windowed app.py
The executable will be created in the dist directory.

Acknowledgments
OpenCV - Open source computer vision and machine learning software library.
MediaPipe - Cross-platform framework for building multimodal applied ML pipelines.

License
This project is licensed under the MIT License - see the LICENSE file for details.

