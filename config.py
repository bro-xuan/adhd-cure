# Camera settings
CAMERA_INDEX = 0
FRAME_WIDTH = 640
FRAME_HEIGHT = 480

# Head pose thresholds (degrees of DEVIATION from calibrated baseline)
YAW_THRESHOLD = 30.0           # abs(yaw - baseline) > this = looking away left/right
PITCH_DOWN_DEVIATION = 15.0    # looking 15°+ further down than baseline = phone
PITCH_UP_DEVIATION = 20.0      # looking 20°+ further up than baseline = away

# Calibration
CALIBRATION_DURATION = 3.0     # seconds to collect baseline samples at startup

# Timing (seconds)
DISTRACTION_GRACE_PERIOD = 3.0   # sustained distraction before first alert
ALERT_COOLDOWN = 10.0            # min time between successive alerts
ESCALATION_INTERVAL = 15.0       # total distraction time to escalate alert level

# MediaPipe confidence
FACE_DETECTION_CONFIDENCE = 0.5
FACE_TRACKING_CONFIDENCE = 0.5

# Alert sounds — cheesy escalation
import os
_SOUNDS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sounds")
SOUND_GENTLE = os.path.join(_SOUNDS_DIR, "navi-hey-listen.mp3")      # L1: Zelda fairy nag
SOUND_MEDIUM = os.path.join(_SOUNDS_DIR, "bruh.mp3")                 # L2: deadpan disappointment
SOUND_AGGRESSIVE = os.path.join(_SOUNDS_DIR, "vine-boom.mp3")        # L3: dramatic meme boom

# Debug
DEBUG_WINDOW = True
LOG_TO_CONSOLE = True
