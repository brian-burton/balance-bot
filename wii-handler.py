import cwiid, time, sys, socket

try:
  #print("Opening socket")
  clientsocket = socket.socket()
  result = -1
  while result != 0:
    result = clientsocket.connect_ex(('localhost', 8088))
    #print(result)
    time.sleep(0.5)
  #print("Socket open")
except Exception as e:
  #print("Couldn't open socket: {0}".format(e))
  sys.exit(1)

wii = None
while not wii:
    try:
        wii = cwiid.Wiimote()
    except:
        pass
        #print("Hold down Wiimote buttons")
#print("Connected to Wiimote")

wii.rpt_mode = cwiid.RPT_ACC | cwiid.RPT_BTN

old_dir = ""
while True:
  buttons = wii.state['buttons']
  if (buttons & cwiid.BTN_UP) and (buttons & cwiid.BTN_LEFT):
    direction = "fl"
  elif (buttons & cwiid.BTN_UP) and (buttons & cwiid.BTN_RIGHT):
    direction = "fr"
  elif (buttons & cwiid.BTN_DOWN) and (buttons & cwiid.BTN_LEFT):
    direction = "bl"
  elif (buttons & cwiid.BTN_DOWN) and (buttons & cwiid.BTN_RIGHT):
    direction = "br"
  elif (buttons & cwiid.BTN_UP):
    direction = "fw"
  elif (buttons & cwiid.BTN_DOWN):
    direction = "bw"
  elif (buttons & cwiid.BTN_LEFT):
    direction = "le"
  elif (buttons & cwiid.BTN_RIGHT):
    direction = "ri"
  else:
    direction = "st"

  if buttons & cwiid.BTN_B:
    direction += "+"
  try:
    if direction != old_dir:
      clientsocket.send(direction.encode())
      old_dir = direction
  except Exception as e:
    pass
    #print("Couldn't send button status: {0}".format(e))
