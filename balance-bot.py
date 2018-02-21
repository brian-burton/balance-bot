import sys
from time import sleep
from envirophat import motion
from explorerhat import motor

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()

try:
  while True:
    x, y, z = motion.accelerometer()
    delta_angle = round(100*(y-BASE_Y))
    motor.speed(delta_angle)
    print(delta_angle)
    sleep(0.1)
except KeyboardInterrupt:
  motor.stop()
  sys.exit()