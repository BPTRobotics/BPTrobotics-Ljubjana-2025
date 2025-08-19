from ...configuration import get_config
import time

try:
    RST_PIN = get_config()['gyroscope']['pin']
except ValueError:
    raise ValueError("gyroscope.pin is not in the config.")

import RPi.GPIO as GPIO


from .setup import init

GPIO.setup(RST_PIN,GPIO.OUT)
GPIO.output(RST_PIN,GPIO.HIGH)

from time import sleep

def reset():
    GPIO.output(RST_PIN,GPIO.LOW)
    sleep(.2)
    GPIO.output(RST_PIN,GPIO.HIGH)
    try:
        init()
    except ValueError:
        print("No I2C Error, sleeping 1s")
        sleep(1)
        init()
    sleep(.75)

last_reset = 0

def safe_reset():
    global last_reset
    now = time.time()
    if now - last_reset > 2:  # 2 seconds between resets
        print("Performing sensor reset...")
        reset()
        last_reset = now
    else:
        print("Reset suppressed — too soon.")
