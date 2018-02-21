import sys
from envirophat import motion
from explorerhat import motor

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()

try:
  while True:
    x, y, z = motion.accelerometer()
    print(x, y, z)
except KeyboardInterrupt:
  motor.stop()
  sys.exit()