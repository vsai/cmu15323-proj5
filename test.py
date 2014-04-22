import scipy
import numpy
import sys

wavefile = sys.argv[1]

print "Running it on %s"%(wavefile)

samplingRate, data = scipy.io.wavfile.read(wavefile)

print samplingRate, data
