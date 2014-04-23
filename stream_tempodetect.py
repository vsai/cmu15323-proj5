#THANKS: http://stackoverflow.com/questions/2648151/python-frequency-detection

# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import sys
import time
import struct
import bucketing_test as bt

WIDTH = 2
CHANNELS = 1
RATE = 44100

# open stream
p = pyaudio.PyAudio()

#def getTapped(indata, frame_count):


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
    note = bt.getNote(freq)
    print note
    return (in_data, pyaudio.paContinue)

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=1024,
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
