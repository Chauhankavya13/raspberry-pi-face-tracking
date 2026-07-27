from picamera2 import Picamera2
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import Device
import mediapipe as mp
import cv2
from time import sleep

Device.pin_factory = PiGPIOFactory()

# ======================================================
# Servo Setup
# ======================================================

pan = AngularServo(
    27,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=0.0005,
    max_pulse_width=0.0025
)

tilt = AngularServo(
    17,
    min_angle=-90,
    max_angle=90,
    min_pulse_width=0.0005,
    max_pulse_width=0.0025
)

PAN_MIN = -70
PAN_MAX = 70

TILT_MIN = -70
TILT_MAX = 50

pan_angle = 0
tilt_angle = -20

pan.angle = pan_angle
tilt.angle = tilt_angle

sleep(1)

# ======================================================
# Camera
# ======================================================

picam2 = Picamera2()

config = picam2.create_preview_configuration(
    main={
        "size": (640,480),
        "format":"RGB888"
    }
)

picam2.configure(config)
picam2.start()

# ======================================================
# Face Mesh
# ======================================================

mesh = mp.solutions.face_mesh.FaceMesh(
    static_image_mode=False,
    max_num_faces=1,
    refine_landmarks=False,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6
)

WIDTH = 480
HEIGHT = 640

CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2

# ======================================================
# Tracking Parameters
# ======================================================

sx = CENTER_X
sy = CENTER_Y

ALPHA = 0.25

KP = 0.03
DEAD = 40

# ======================================================
# Hunt Mode
# ======================================================

face_missing = 0

HUNT_DELAY = 40

hunt_direction = 1

HUNT_SPEED = 0.4

print("FT8 Started")

# ======================================================
# Main Loop
# ======================================================

while True:

    frame = picam2.capture_array()

    frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    frame = cv2.flip(frame,0)

    results = mesh.process(frame)

    cv2.circle(frame,(CENTER_X,CENTER_Y),4,(255,0,0),-1)

    if results.multi_face_landmarks:

        face_missing = 0

        face = results.multi_face_landmarks[0]

        # ---------------- LEFT EYE ----------------

        LEFT_EYE = [33,133]

        lx = 0
        ly = 0

        for p in LEFT_EYE:

            lm = face.landmark[p]

            lx += lm.x
            ly += lm.y

        lx /= len(LEFT_EYE)
        ly /= len(LEFT_EYE)

        # ---------------- RIGHT EYE ----------------

        RIGHT_EYE = [362,263]

        rx = 0
        ry = 0

        for p in RIGHT_EYE:

            lm = face.landmark[p]

            rx += lm.x
            ry += lm.y

        rx /= len(RIGHT_EYE)
        ry /= len(RIGHT_EYE)

        eye_x = (lx + rx) / 2
        eye_y = (ly + ry) / 2

        # ---------------- NOSE ----------------

        NOSE = [1,4,5,6,168,195,197]

        nx = 0
        ny = 0

        for p in NOSE:

            lm = face.landmark[p]

            nx += lm.x
            ny += lm.y

        nx /= len(NOSE)
        ny /= len(NOSE)

        # ---------------- BLEND ----------------

        track_x = eye_x * 0.7 + nx * 0.3
        track_y = eye_y * 0.7 + ny * 0.3

        cx = int(track_x * WIDTH)
        cy = int(track_y * HEIGHT)

        cv2.circle(frame,(cx,cy),6,(0,255,0),-1)

        # ---------------- SMOOTH ----------------

        sx = ALPHA * cx + (1-ALPHA) * sx
        sy = ALPHA * cy + (1-ALPHA) * sy

        cv2.circle(frame,(int(sx),int(sy)),5,(0,0,255),-1)

        ex = sx - CENTER_X
        ey = sy - CENTER_Y        # ======================================================
        # PAN CONTROL
        # ======================================================

        if abs(ex) > DEAD:
            pan_angle += ex * KP

        # ======================================================
        # TILT CONTROL
        # ======================================================

        if abs(ey) > DEAD:
            tilt_angle += ey * KP

        # ======================================================
        # LIMIT SERVO ANGLES
        # ======================================================

        if pan_angle > PAN_MAX:
            pan_angle = PAN_MAX

        if pan_angle < PAN_MIN:
            pan_angle = PAN_MIN

        if tilt_angle > TILT_MAX:
            tilt_angle = TILT_MAX

        if tilt_angle < TILT_MIN:
            tilt_angle = TILT_MIN

        # ======================================================
        # MOVE SERVOS
        # ======================================================

        if pan.angle is None or abs(pan.angle - pan_angle) >= 0.5:
            pan.angle = pan_angle

        if tilt.angle is None or abs(tilt.angle - tilt_angle) >= 0.5:
            tilt.angle = tilt_angle

    else:

        # ======================================================
        # HUNT MODE
        # ======================================================

        face_missing += 1

        if face_missing > HUNT_DELAY:

            pan_angle += hunt_direction * HUNT_SPEED

            if pan_angle >= PAN_MAX:
                pan_angle = PAN_MAX
                hunt_direction = -1

            elif pan_angle <= PAN_MIN:
                pan_angle = PAN_MIN
                hunt_direction = 1

            if pan.angle is None or abs(pan.angle - pan_angle) >= 0.5:
                pan.angle = pan_angle

        cv2.putText(
            frame,
            "SEARCHING...",
            (10,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,0,255),
            2
        )

    # ======================================================
    # DISPLAY
    # ======================================================

    cv2.putText(
        frame,
        f"Pan : {pan_angle:.1f}",
        (10,25),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Tilt: {tilt_angle:.1f}",
        (10,50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (255,255,255),
        2
    )

    if face_missing <= HUNT_DELAY:

        cv2.putText(
            frame,
            "TRACKING",
            (10,80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0,255,0),
            2
        )

    cv2.imshow(
        "FT8 Face Tracking",
        frame
    )    # ======================================================
    # Exit Key
    # ======================================================

    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):
        break

# ======================================================
# Cleanup
# ======================================================

print("Stopping...")

pan.angle = 0
tilt.angle = -20

sleep(0.5)

picam2.stop()

cv2.destroyAllWindows()