# Installation Guide

## Prerequisites

Before running this project, ensure you have the following:

* Raspberry Pi 4 Model B
* Raspberry Pi OS (Bookworm or newer)
* Raspberry Pi Camera Module
* Python 3.11 or later
* Internet connection (for installing packages)

## Clone the Repository

```bash
git clone https://github.com/Chauhankavya13/raspberry-pi-face-tracking.git
cd raspberry-pi-face-tracking
```

## Create a Virtual Environment (Recommended)

```bash
python3 -m venv faceenv
source faceenv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

If you do not have a requirements file yet, install the libraries manually:

```bash
pip install opencv-python mediapipe gpiozero numpy
```

Install Picamera2:

```bash
sudo apt update
sudo apt install python3-picamera2
```

## Enable the Camera

Open Raspberry Pi Configuration or run:

```bash
sudo raspi-config
```

Navigate to:

```
Interface Options
→ Camera
→ Enable
```

Restart the Raspberry Pi.

## Connect Hardware

* Connect the Raspberry Pi Camera to the CSI port.
* Connect the pan servo to GPIO 27.
* Connect the tilt servo to GPIO 17.
* Use an external 5V supply for the servos.
* Connect all grounds together.

## Run the Project

```bash
python3 face_tracking.py
```

The camera window will open and the servos will begin tracking detected faces.
