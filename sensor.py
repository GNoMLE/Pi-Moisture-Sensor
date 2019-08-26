import time
import sys

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(SCL, SDA)

sensors = [ Seesaw(i2c_bus, addr=addr) for addr in [0x36, 0x39]]

while True:
    for i, sensor in enumerate(sensors):
        try:
            touch = sensor.moisture_read()
            temp = sensor.get_temp()
            now = time.time()
            print("%f,%d,%f,%d" % (now, i, temp, touch))
            sys.stdout.flush()

        except:
            pass

        time.sleep(1)
