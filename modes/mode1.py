from ..control import servo
PITCH_SENSITIVITY = 10
def start():
    while True:
        
        normalized_steer = min(max(-1,PITCH_SENSITIVITY / 10),1)

        servo.steer(normalized_steer)
        print("Pitch:",pitch)