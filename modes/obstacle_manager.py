from . import mode3
from ..sensors import gyroscope

def start():    
    gyroscope.calibrate()
    gyroscope.INITIAL_DIRECTION.value = gyroscope.get_safe_pitch()
    mode3()