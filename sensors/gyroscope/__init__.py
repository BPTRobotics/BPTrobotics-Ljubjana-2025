from .setup import i2c, sensor       
from . import utils                  
from .utils import *                 

def get_pitch():
    try:
        return utils.get_pitch(sensor)
    except KeyError as e:
        print(f"Key error: {e}")
