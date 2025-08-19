from .direction_manager import keep_direction
from ..sensors import gyroscope
from ..control import motor
from time import sleep

def start():
    gyroscope.INITIAL_DIRECTION += 90
    pitch_difference = 999

    motor.set_speed(1)
    motor.backward()
    while (pitch_difference or 10) > 10:
        pitch_difference = keep_direction()
        if pitch_difference is not None:
            motor.backward()
            print(f"MODE (2): Pitch difference: {pitch_difference:.2f}")
        else:
            motor.stop()
    motor.stop()