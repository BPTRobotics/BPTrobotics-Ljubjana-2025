from .setup import sensor, INITIAL_DIRECTION
from . import utils                  
from .utils import *        
from ._reset import reset, safe_reset
from ._calibrate import calibrate

def get_pitch():
    try:
        return utils.get_pitch(sensor)
    except (KeyError, ValueError) as e:
        print(f"Key / Value error: {e}")
def get_safe_pitch():
    pitch = get_pitch()
    if pitch is None:
        safe_reset()
    return pitch