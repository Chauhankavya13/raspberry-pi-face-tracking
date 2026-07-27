# Software

## Programming Language

* Python 3

## Development Environment

* Raspberry Pi OS
* Visual Studio Code
* Terminal

## Libraries Used

* OpenCV
* MediaPipe
* Picamera2
* gpiozero
* NumPy

## Project Structure

```
raspberry-pi-face-tracking/
│
├── face_tracking.py
├── README.md
├── requirements.txt
├── images/
├── videos/
├── circuit/
└── docs/
```

## Face Detection

MediaPipe Face Detection is used to identify faces in each video frame.

## Camera Interface

Picamera2 captures live video from the Raspberry Pi Camera.

## Servo Control

The detected face coordinates are converted into servo movement commands, allowing the camera to continuously follow the target.

## Image Processing

OpenCV performs frame capture, image conversion, drawing bounding boxes, and displaying the live video.
