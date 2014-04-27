import OSC
import time, random

#REQUIRES ip_addr as string, port as number
def osc_setup(ip_addr, port=7770):
    send_address = (ip_addr, port)
    c = OSC.OSCClient()
    c.connect( send_address ) # set the address for all following messages
    return c

def osc_send_midi(c, channel_name, midi_note):
    msg = OSC.OSCMessage()
    channel = "/midi" + channel_name
    msg.setAddress(channel) # set OSC address
    msg.append(midi_note) # int
    c.send(msg) # send it!

