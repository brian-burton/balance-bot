import socket, sys, time
from envirophat import motion
from explorerhat import motor

BASE_X, BASE_Y, BASE_Z = motion.accelerometer()
motor.one.invert()

try:
  socketserver = socket.socket()
  socketserver.bind(('localhost', 8088))
  socketserver.listen(5)
except Exception as e:
  print("Broke the sockets, probably: {0}".format(e))
  sys.exit(1)

try:
  connection = None
  while not connection:
    print("Waiting for connection")
    connection, address = socketserver.accept()
  while True:
    socketdata = connection.recv(2).decode()
    if len(socketdata) > 0:
      if socketdata == "fl":
        motor.one.forwards(20)
        motor.two.forwards(10)
      elif socketdata == "fr":
        motor.one.forwards(10)
        motor.two.forwards(20)
      elif socketdata == "fw":
        motor.forwards(20)
      elif socketdata == "br":
        motor.one.backwards(10)
        motor.two.backwards(20)
      elif socketdata == "bl":
        motor.one.backwards(20)
        motor.two.backwards(10)
      elif socketdata == "bw":
        motor.backwards(20)
      elif socketdata == "le":
        motor.one.forwards(20)
        motor.two.backwards(20)
      elif socketdata == "ri":
        motor.one.backwards(20)
        motor.two.forwards(20)
      elif socketdata == "st":
        motor.stop()


      print(socketdata)
except KeyboardInterrupt:
  print("Successful shutdown")
except:
  print("Broke the explorer pHAT somehow")
finally:
  motor.stop()
  socketserver.shutdown(socket.SHUT_RDWR)
  socketserver.close()
