import OSC
import time, random

send_address = ('127.0.0.1', 7770)

# OSC basic client
c = OSC.OSCClient()
c.connect( send_address ) # set the address for all following messages

# single message
msg = OSC.OSCMessage()
msg.setAddress("/midi") # set OSC address
msg.append(44) # int

c.send(msg) # send it!
