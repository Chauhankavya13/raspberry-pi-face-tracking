# Working Principle

## Step 1 – Capture Video

The Raspberry Pi Camera continuously captures live video frames.

## Step 2 – Detect Face

Each frame is processed using MediaPipe Face Detection to locate the face.

## Step 3 – Calculate Position

The centre point of the detected face is calculated.

## Step 4 – Compare with Frame Centre

The system compares the face position with the centre of the camera frame.

## Step 5 – Move Servos

If the face moves:

* Left → Pan servo rotates left.
* Right → Pan servo rotates right.
* Up → Tilt servo moves upward.
* Down → Tilt servo moves downward.

## Step 6 – Repeat

The process repeats continuously to provide smooth real-time face tracking.

## System Flow

```
Camera
   ↓
Capture Frame
   ↓
MediaPipe Face Detection
   ↓
Calculate Face Coordinates
   ↓
Servo Control Algorithm
   ↓
Pan-Tilt Camera Movement
   ↓
Repeat
```
