from .direction_manager import keep_direction
from ..control import motor
from ..sensors import lidar
from time import sleep

msg = None
def callback(__msg):
    global msg
    msg = __msg

DISTANCE_= .75

def start():
    global msg

    lidar.setup.init(callback)
    motor.set_speed(1)
    distance = 0

    while True:
        pitch_diff = keep_direction()
        motor.forward()
        if pitch_diff is None: motor.stop()
        else: motor.backward()

        if pitch_diff: print(f"MODE (1): Pitch difference: {pitch_diff:.2f}")

        if msg: distance = lidar.utils.extract_distance(180,msg)
        else: 
            motor.stop()
            continue
        
        if (distance or DISTANCE_) < DISTANCE_:
            break

        sleep(0.05)