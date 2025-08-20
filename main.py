from . import modes
from .sensors import gyroscope
from .control import servo, motor
import RPi.GPIO as GPIO
import rospy
import signal
import sys

ROUNDS = 3

def cleanup():
    print("Cleaning up: stopping motors, servos, ROS, GPIO...")
    servo.stop()
    motor.stop()
    if rospy.core.is_initialized():
        rospy.signal_shutdown("Program exiting")
    GPIO.cleanup()


def signal_handler(sig, frame):
    print("Ctrl+C pressed. Exiting gracefully...")
    cleanup()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)  


gyroscope.calibrate()
gyroscope.INITIAL_DIRECTION.value = gyroscope.get_safe_pitch()


try:
    for _ in range(ROUNDS*4):
        modes.mode1()
        modes.mode2()

        print(ROUNDS,"round has succesfully completed. 🚩")
except Exception as e:
    print(f"Exception occurred: {e}")
    cleanup()
    sys.exit(1)


cleanup()
