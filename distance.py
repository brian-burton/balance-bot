import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

TRIG = 17
ECHO = 18
print("Distance Measurement In Progress")
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.output(TRIG, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

def measure():
    pulse_duration = 0
    for i in range(5):
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)
        while GPIO.input(ECHO)==0:
            pulse_start = time.time()
        while GPIO.input(ECHO)==1:
            pulse_end = time.time()
#            print(pulse_end - pulse_start)
        pulse_duration += (pulse_end - pulse_start)
    pulse_duration /= 5
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance

try:
    while True:
        dist = measure()
        print("Distance: {}cm".format(dist))
        time.sleep(0.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
