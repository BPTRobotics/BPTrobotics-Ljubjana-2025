from ..control import servo
from ..sensors import gyroscope

PITCH_SENSITIVITY = 10

def keep_direction():
    pitch = gyroscope.get_safe_pitch()
    
    if not pitch: return pitch
    
    pitch_difference = gyroscope.angle_difference(pitch, gyroscope.INITIAL_DIRECTION)

    normalized_steer = min(max(-1, pitch_difference / PITCH_SENSITIVITY), 1)

    print(f"Pitch difference: {pitch_difference}",pitch, gyroscope.INITIAL_DIRECTION)

    servo.safe_steer(normalized_steer)

    return pitch