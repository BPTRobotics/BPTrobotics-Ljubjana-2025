from configuration import get_config

try:
    config = get_config()

    CHANNEL = config['servo']['CHANNEL']
except KeyError:
    raise KeyError("""
          Configuration error:
          servo.CHANNEL is not availible
          """)
    

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)


