import socket, sys, time
from envirophat import motion
from explorerhat import motor
from explorerhat import input

prox_stop = 0

def proxalert(input):
    global prox_stop
    prox_stop = input.read()
    if prox_stop == 1:
        motor.stop()

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()
motor.one.invert()

input.one.changed(proxalert)

try:
  socketserver = socket.socket()
  socketserver.bind(('localhost', 8088))
  socketserver.listen(5)
except Exception as e:
  #print("Broke the sockets, probably: {0}".format(e))
  sys.exit(1)

try:
  connection = None
  while not connection:
    #print("Waiting for connection")
    connection, address = socketserver.accept()
  while True:
    socketdata = connection.recv(3).decode()
    if (len(socketdata) > 0):
      if (socketdata == "fl") and (prox_stop == 0):
        motor.one.forwards(100)
        motor.two.stop()
      elif socketdata == "fr" and (prox_stop == 0):
        motor.one.stop()
        motor.two.forwards(100)
      elif socketdata == "fw" and (prox_stop == 0):
        motor.forwards(100)
      elif socketdata == "br":
        motor.one.stop()
        motor.two.backwards(100)
      elif socketdata == "bl":
        motor.one.backwards(100)
        motor.two.stop()
      elif socketdata == "bw":
        motor.backwards(100)
      elif socketdata == "le":
        motor.one.forwards(100)
        motor.two.backwards(100)
      elif socketdata == "ri":
        motor.one.backwards(100)
        motor.two.forwards(100)
      elif socketdata == "st":
        motor.stop()
    elif prox_stop == 1:
      motor.stop()
    #print(socketdata)
except KeyboardInterrupt:
  pass
  #print("Successful shutdown")
except:
  pass
  #print("Broke the explorer pHAT somehow")
finally:
  motor.stop()
  socketserver.shutdown(socket.SHUT_RDWR)
  socketserver.close()
