# Hardware

## Project Overview

This project is a real-time face tracking system that detects a person's face using the Raspberry Pi Camera and MediaPipe. Two SG90 servo motors move a pan-tilt mechanism to keep the detected face centred in the camera frame.

## Components Used

| Component                  |    Quantity |
| -------------------------- | ----------: |
| Raspberry Pi 4 Model B     |           1 |
| Raspberry Pi Camera Module |           1 |
| SG90 Servo Motor           |           2 |
| Pan-Tilt Camera Mount      |           1 |
| External 5V Power Supply   |           1 |
| Jumper Wires               | As Required |

## GPIO Connections

| Component         | Raspberry Pi Pin |
| ----------------- | ---------------- |
| Pan Servo Signal  | GPIO 27          |
| Tilt Servo Signal | GPIO 17          |
| Camera            | CSI Port         |
| Servo VCC         | pi 4 pin of 5V   |
| Servo GND         | Common Ground    |

## Wiring Diagram

The wiring diagram is available in the **circuit/** folder.

## Hardware Setup

Images of the completed hardware setup are available in the **images/** folder.
