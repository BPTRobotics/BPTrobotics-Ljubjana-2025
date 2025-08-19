from .direction_manager import keep_direction
from ..control import motor

def start():
    motor.set_speed(1)
    while True:
        pitch = keep_direction()
        if pitch is None: motor.stop()
        else: motor.forward()