import board
import busio
from adafruit_bno08x.i2c import BNO08X_I2C
from adafruit_bno08x import (
    BNO_REPORT_ACCELEROMETER,
    BNO_REPORT_GYROSCOPE,
    BNO_REPORT_ROTATION_VECTOR
)

# Set up I2C communication
i2c = busio.I2C(board.SCL, board.SDA, frequency=400000)
sensor = BNO08X_I2C(i2c, address=0x4B)

# Enable required features
sensor.enable_feature(BNO_REPORT_ACCELEROMETER)
sensor.enable_feature(BNO_REPORT_GYROSCOPE)
sensor.enable_feature(BNO_REPORT_ROTATION_VECTOR)