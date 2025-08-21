from ..sensors import lidar
from ctypes import c_float
import time

msg = None
def callback(__msg):
    global msg
    msg = __msg

lidar.setup.init(callback)

while not msg:
    lidar.utils.sleep(.5)

sd = lidar.utils.extract_distance(180, msg)
print("START DISTANCE:", sd)
START_DISTANCE = c_float(sd)