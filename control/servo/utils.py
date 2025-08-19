from .setup import kit, CHANNEL

def set_angle(angle):
    kit.servo[CHANNEL].angle = angle