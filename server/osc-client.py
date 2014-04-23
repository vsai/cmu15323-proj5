import OSC
import time, random

#REQUIRES ip_addr as string, port as number
def osc_setup(ip_addr, port):
    send_address = (ip_addr, port)
    c = OSC.OSCClient()
    c.connect( send_address ) # set the address for all following messages

def osc_send_midi(midi_note):
    msg = OSC.OSCMessage()
    msg.setAddress("/midi") # set OSC address
    msg.append(44) # int
    c.send(msg) # send it!

