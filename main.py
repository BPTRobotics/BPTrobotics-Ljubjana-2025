from . import modes
from .sensors import gyroscope
from .control import servo
from atexit import register as areg
import RPi.GPIO as GPIO

def cleanup():
    servo.stop()
    GPIO.cleanup()
areg(cleanup)

gyroscope.calibrate()
gyroscope.INITIAL_DIRECTION = gyroscope.get_safe_pitch()

modes.mode1()