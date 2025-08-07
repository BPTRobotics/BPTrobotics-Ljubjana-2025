from math import atan2, degrees

def quaternion_to_euler(qw, qx, qy, qz):
    pitch = atan2(2.0 * (qw * qy + qx * qz), 1.0 - 2.0 * (qx**2 + qy**2))    
    return degrees(pitch)

def get_pitch(sensor):
    try:
        qw, qx, qy, qz = sensor.quaternion  
        return quaternion_to_euler(qw, qx, qy, qz)
    except KeyError as e:
        print(f"Key error: {e}")
    except Exception as e:
        print(f"Error occurred while reading quaternion: {e}")
