#THANKS: http://stackoverflow.com/questions/3694918/how-to-extract-frequency-associated-with-fft-values-in-python
import wave
import struct
import numpy as np

import sys

if __name__=='__main__':
    if (len(sys.argv)<2):
        print "no wav file arg inputted"
        sys.exit(-1)
    
    fname=sys.argv[1]
    wf = wave.open(fname, 'rb')
    data_size=wf.getnframes()
    frate=wf.getframerate()
    data=wf.readframes(data_size)
    wf.close()

    data=struct.unpack('{n}h'.format(n=data_size), data)
    data=np.array(data)                                
    w = np.fft.fft(data)
    freqs = np.fft.fftfreq(len(w))
    #print(freqs.min(),freqs.max())
    
    # Find the peak in the coefficients
    idx=np.argmax(np.abs(w)**2)
    freq=freqs[idx]
    freq_in_hertz=abs(freq*frate)
    print(freq_in_hertz)
