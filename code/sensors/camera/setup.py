import time
from .huskylib import HuskyLensLibrary

from ...configuration import get_config


NOISE_THRESHOLD = get_config().get('Camera', {}).get('noise_threshold', None)
if NOISE_THRESHOLD is None:
    print("Camera.noise_threshold is not configured")
    NOISE_THRESHOLd = 1000

SERIAL_PORT = "/dev/my_HuskyCam"
BAUD_RATE = 3000000

hl = HuskyLensLibrary("SERIAL", SERIAL_PORT, BAUD_RATE)

hl.algorthim("ALGORITHM_COLOR_RECOGNITION")