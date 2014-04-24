import wave
import sys
import numpy as np

if (len(sys.argv)<2):
    print "Enter a valid wave file.\r\n Usage: %s filename.wav"%(sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')

print "number of channels: %d"%(wf.getnchannels())
print "sample width: %d"%(wf.getsampwidth())
print "sampling frequency: %d"%(wf.getframerate())
print "number of audio frames: %d"%(wf.getnframes())
print "compression type: %s"%(wf.getcompname())

data = wf.readframes(wf.getnframes())

print "type(data): %s"%(type(data))
print "len(data): %s"%(len(data))

print "sampwidth * audioframes = %d"%(wf.getsampwidth() * wf.getnframes())
print "num seconds = %d"%(wf.getnframes() / wf.getframerate())

nchannels = wf.getnchannels()
sig = np.frombuffer(data, dtype='<i2').reshape(-1, nchannels)
print "original signal dimensions: numrows: %d, numcols: %d"%(len(sig), len(sig[0]))

sig = sig.flatten()
print "type(sig): %s"%(type(sig))
print "len(sig): %s"%(len(sig))

fourier = np.fft.fft(sig)
n = sig.size
timestep = 1.0/44100
freq = np.fft.fftfreq(n, d=timestep)

print "len(freq) = %d"%(len(freq))
print "Printing frequency buckets"

print np.amax(fourier)
print np.amax(freq)
wf.close()


