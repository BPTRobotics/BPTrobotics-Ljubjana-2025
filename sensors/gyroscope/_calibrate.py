from .. import gyroscope
from .utils import angle_difference
def calibrate():
    pitch = gyroscope.get_safe_pitch()
    latest_pitch = -999
    attempt = 10
    while attempt > 0:
        pitch = gyroscope.get_safe_pitch()
        if angle_difference(pitch,latest_pitch) < 1:
            break
        attempt -= 1
        latest_pitch = pitch