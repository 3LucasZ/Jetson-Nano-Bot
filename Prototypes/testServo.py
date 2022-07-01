from adafruit_servokit import ServoKit
from board import SCL, SDA
import busio
import time

print("Initialize i2c")
i2c_bus=busio.I2C(SCL, SDA)
print("Initialize pins")
kit = ServoKit(channels=16, i2c=i2c_bus)
print("Sweep test")
sweep = range(0,180)
for degree in sweep:
    kit.servo[15].angle=degree

quit()
print("Code finished")