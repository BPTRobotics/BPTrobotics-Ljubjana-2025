from . import modes
from .sensors import gyroscope
from .control import servo, motor
import RPi.GPIO as GPIO
import rospy
import signal
import sys

ROUNDS = 1/4

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
    modes.mode1()
    modes.detect_direction()
    modes.mode2()
    for rnd in range(int(ROUNDS * 4 - 1)):
        modes.mode1()
        modes.mode2()

        print(rnd,"round has succesfully completed. 🚩")
    
    modes.mode1(modes.lidar_manager.START_DISTANCE.value)
except Exception:
    import traceback
    traceback.print_exc()
    cleanup()
    sys.exit(1)


cleanup()
