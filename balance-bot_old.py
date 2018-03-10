import sys
from time import sleep
from envirophat import motion
from explorerhat import motor

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()
motor.one.invert()

try:
  while True:
    x, y, z = motion.accelerometer()
    delta_angle = round(100*(y-BASE_Y))
    if delta_angle < 0:
      motor.backwards(min(100, 4*abs(delta_angle)))
    elif delta_angle > 0:
      motor.forwards(min(100, 4*delta_angle))
    else:
      motor.stop()
    # clamp motor speed between -100 and 100
    # motor.speed(min(100,max(-100,2*delta_angle)))
    print(delta_angle)
    sleep(0.05)
except KeyboardInterrupt:
  motor.stop()
  sys.exit()
