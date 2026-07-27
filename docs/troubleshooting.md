# Troubleshooting

## Camera Not Detected

Check that:

* The camera cable is connected correctly.
* The camera is enabled.
* The Raspberry Pi has been restarted.

---

## No Module Named "picamera2"

Install:

```bash
sudo apt install python3-picamera2
```

---

## Servo Jitter

Possible causes:

* Powering servos directly from the Raspberry Pi.
* Weak power supply.

Recommended solution:

* Use an external 5V supply.
* Connect all grounds together.

---

## MediaPipe Installation Error

Upgrade pip:

```bash
pip install --upgrade pip
```

Install MediaPipe again:

```bash
pip install mediapipe
```

---

## Low FPS

Possible solutions:

* Reduce camera resolution.
* Close unnecessary applications.
* Improve lighting conditions.

---

## Face Not Detected

* Ensure adequate lighting.
* Keep the face within the camera frame.
* Avoid excessive camera movement.
