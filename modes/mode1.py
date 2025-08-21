from .direction_manager import keep_direction
from ..control import motor
from ..sensors import lidar
from time import sleep
from ..sensors.gyroscope import INITIAL_DIRECTION
from . import lidar_manager


def start(DISTANCE_ = 1.1):
    global lidar_manager
    motor.set_speed(1)
    distance = 0

    while True:
        pitch_diff = keep_direction()
        if pitch_diff is None: motor.stop()
        else: motor.backward()

        if pitch_diff and INITIAL_DIRECTION.value: print(f"MODE (1): Pitch difference: {pitch_diff:.2f} INITIAL_DIRECTION: {INITIAL_DIRECTION.value:.2f}")

        if lidar_manager.msg: distance = lidar.utils.extract_distance(180,lidar_manager.msg)
        else: 
            motor.stop()
            continue
        
        if (distance or DISTANCE_) < DISTANCE_:
            break

        sleep(0.05)
    motor.stop()