import explorerhat

def changed(input):
  state = input.read()
  name  = input.name
  print("Input {} changed to {}".format(name,state))
  
explorerhat.input.one.changed(changed)

explorerhat.pause()
