from ..control import servo
from ..sensors import gyroscope

PITCH_SENSITIVITY = 20

def keep_direction():
    pitch = gyroscope.get_safe_pitch()
    
    if pitch is None: return None
    
    pitch_difference = gyroscope.angle_difference(pitch, gyroscope.INITIAL_DIRECTION)

    normalized_steer = min(max(-1, pitch_difference / PITCH_SENSITIVITY), 1)

    servo.safe_steer(-normalized_steer)

    return pitch_difference