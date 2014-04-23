import wave
import sys
import numpy as np
#from utility import pcm2float

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
#sig = np.frombuffer(data, dtype='<i2').reshape(-1, nchannels)
sig = np.frombuffer(data, dtype='float').reshape(-1, nchannels)
print "original signal dimensions: numrows: %d, numcols: %d"%(len(sig), len(sig[0]))

sig = sig.flatten()
print "type(sig): %s"%(type(sig))
print "len(sig): %s"%(len(sig))
print sig[0:100]

#normalized = pcm2float(sig, np.float32)
#print "type(normalized): %s"%(type(normalized))
#print "len(normalized): %s"%(len(normalized))

fourier = np.fft.fft(sig)

for i in range(10):
    print fourier[i]



n = sig.size
timestep = 1.0/44100
freq = np.fft.fftfreq(n, d=timestep)

print "PLOTTING"

print fourier[0:100]
print freq[0:100]

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
p = ax.plot(freq, fourier, 'b')
ax.set_xlabel('frequencies')
ax.set_ylabel('fourier values')


wf.close()

fig.show()

plt.show()

#wf.close()


