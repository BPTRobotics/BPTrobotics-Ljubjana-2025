
from . import modes
from .sensors import gyroscope
from .control import servo
import RPi.GPIO as GPIO
from atexit import register as areg
def cleanup():
    servo.stop()
    GPIO.cleanup()
areg(cleanup)


gyroscope.calibrate()
gyroscope.INITIAL_DIRECTION = gyroscope.get_safe_pitch()

try:
    for _ in range(12):
        modes.mode1()
        modes.mode2()
except KeyboardInterrupt:
    print("Cancelled ^C")