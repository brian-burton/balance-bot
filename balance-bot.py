import sys
from time import sleep
from envirophat import motion
from explorerhat import motor
from pid_controller.pid import PID

PROPORTIONAL = 3
INTEGRAL = 0.2
DIFFERENTIAL = 0

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()
motor.one.invert()
pid=PID(PROPORTIONAL, INTEGRAL, DIFFERENTIAL)
prev_error = 0

try:
  while True:
    x, y, z = motion.accelerometer()
    error = round(100*(x-BASE_X))
    motorspeed = pid(error)
    print(motorspeed)
    if error != prev_error:
      if motorspeed < 0:
        motor.backwards(min(100, abs(motorspeed)))
      elif motorspeed > 0:
        motor.forwards(min(100, motorspeed))
      else:
        motor.stop()
    prev_error = error
    sleep(0.05)
except KeyboardInterrupt:
  motor.stop()
  sys.exit()
