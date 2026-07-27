# raspberry-pi-face-tracking
Real-time face tracking system using Raspberry Pi, OpenCV, MediaPipe, and servo motors.

A real-time face tracking system built using **Raspberry Pi 4**, **OpenCV**, **MediaPipe**, and a **2-axis pan-tilt mechanism** driven by SG90 servo motors. The system detects a person's face through the Raspberry Pi Camera and automatically adjusts the camera position to keep the face centred in the frame.

---

## 📸 Project Preview

> ![image alt](https://github.com/Chauhankavya13/raspberry-pi-face-tracking/blob/ea790f76b0cdd460ae7ca9dab1be32569acbda60/videos/setup.jpg)


 Hardware Setup     

![image alt](https://github.com/Chauhankavya13/raspberry-pi-face-tracking/blob/d5090ff78b606f25c66676533d92f5ae1e6b0c80/circuit/diagram.png) 

 Face Tracking Demo    
 
## 🎥 Demo Video

▶️ **Watch on YouTube:** https://youtube.com/shorts/GvtiMopBgYA?si=qDI65ewmWpE1aYCI

## 🎥 Demo Video

Watch the project in action:

📹 **Demo:** `videos/demo.mp4`

*(You can also upload the video to YouTube and paste the link here.)*

---

# ✨ Features

* 🎯 Real-time face detection
* 📷 Raspberry Pi Camera integration
* 🤖 Automatic pan-tilt camera movement
* ⚡ Smooth servo control
* 🐍 Python-based implementation
* 👁️ OpenCV image processing
* 🧠 MediaPipe Face Detection
* 💻 Lightweight and easy to run

---

# 🛠 Hardware Used

| Component                  |    Quantity |
| -------------------------- | ----------: |
| Raspberry Pi 4 Model B     |           1 |
| Raspberry Pi Camera Module |           1 |
| SG90 Servo Motor           |           2 |
| Pan-Tilt Mount             |           1 |
| External 5V Power Supply   |           1 |
| Jumper Wires               | As Required |

---

# 💻 Software Used

* Python 3
* OpenCV
* MediaPipe
* Picamera2
* gpiozero
* NumPy

---

# 📂 Project Structure

```text
raspberry-pi-face-tracking/
│
├── face_tracking.py
├── README.md
├── requirements.txt
├── LICENSE
│
├── images/
├── videos/
├── circuit/
└── docs/
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Chauhankavya13/raspberry-pi-face-tracking.git
```

Go to the project directory

```bash
cd raspberry-pi-face-tracking
```

Install the required libraries

```bash
pip install -r requirements.txt
```

Run the project

```bash
python3 face_tracking.py
```

---

# 🧠 How It Works

1. Raspberry Pi Camera captures live video.
2. OpenCV processes each frame.
3. MediaPipe detects the face.
4. Face coordinates are calculated.
5. Servo motors receive movement commands.
6. The pan-tilt mechanism follows the detected face in real time.

---

# 🔌 Wiring Diagram

The complete wiring diagram is available in the **circuit/** folder.

---

# 📚 Documentation

Detailed documentation is available in the **docs/** folder.

* Installation Guide
* Hardware Details
* Software Overview
* Working Principle
* Troubleshooting
* Future Improvements

---

# 🚀 Future Improvements

* Face Recognition
* Object Tracking
* Multi-Face Tracking
* PID-based Servo Control
* Web Dashboard
* Mobile App Control
* Gesture Recognition

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Kavya Chauhan**

Electronics & Communication Engineering Student

Interested in Embedded Systems, Raspberry Pi, IoT, Computer Vision, and Embedded Firmware Development.

GitHub: https://github.com/Chauhankavya13

---

## ⭐ Support

If you found this project helpful, consider giving it a **⭐ Star** on GitHub.
