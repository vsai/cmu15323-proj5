#THANKS: http://stackoverflow.com/questions/2648151/python-frequency-detection

# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import sys
import time
import struct
import freq_bucketing as bt
#import OSC
from client import osc_client as oscc

#settings for OSC
IPADDR = '128.237.172.70'
PORT = 7770
conn = oscc.osc_setup(IPADDR, PORT)
CHANNEL_NAME = raw_input("Enter your midi channel name (1 or 2):")

# settings for pyaudio - open stream
WIDTH = 2
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

def getMainFreq(indata, frame_count):
    # Take the fft and square each value
    fftData = abs(np.fft.rfft(indata))**2
    # find the maximum
    which = fftData[1:].argmax() + 1
    # use quadratic interpolation around the max
    if which != len(fftData)-1:
        y0,y1,y2 = np.log(fftData[which-1:which+2:])
        x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
        # find the frequency and output it
        thefreq = (which+x1)*RATE/frame_count
        #print "The freq is %f Hz." % (thefreq)
    else:
        thefreq = which*RATE/frame_count
        #print "The freq is %f Hz." % (thefreq)
    return thefreq

def callback(in_data, frame_count, time_info, status):
    window = np.blackman(frame_count)
    # unpack the data and times by the hamming window
    indata = np.array(wave.struct.unpack('{n}h'.format(n=frame_count), in_data))*window
    freq = getMainFreq(indata, frame_count)
    note = bt.getMusic(freq, "note")
    print note
    midiNote = bt.getMusic(freq, "midi")
    oscc.osc_send_midi(conn, CHANNEL_NAME, midiNote)
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=False,
                frames_per_buffer=4096,
                stream_callback=callback)

#start the stream
stream.start_stream()

#wait for stream to finish
while stream.is_active():
    time.sleep(0.1)

#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()
