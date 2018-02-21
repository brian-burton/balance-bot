import sys, time
from envirophat import motion
from explorerhat import motor

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()

try:
  while True:
    x, y, z = motion.accelerometer()
    print(round(100*y)
    time.sleep(0.2)
except KeyboardInterrupt:
  motor.stop()
  sys.exit()