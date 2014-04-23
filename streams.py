import pyaudio
import wave
import time
import sys

#if len(sys.argv) < 2:
#    print("Plays a wave file.\n\nUsage: %s filename.wav" % sys.argv[0])
#    sys.exit(-1)

#wf = wave.open(sys.argv[1], 'rb')

# instantiate PyAudio (1)
p = pyaudio.PyAudio()


WIDTH = 2
CHANNELS = 1
RATE = 44100
# define callback (2)
def callback(in_data, frame_count, time_info, status):
    #print in_data
    #print "len(in_data) = %d"%(len(in_data))
    print "frame_count = %d"%(frame_count)
    print "time_info = %s"%(time_info)
    print "status = %s"%(status)

    return (in_data, pyaudio.paContinue)
    #samplingRate, data = scipy.io.wavfile.read(frame_count)
    #data = wf.readframes(frame_count)
    #print type(data), type(data[0])
    #return (data, pyaudio.paContinue)

# open stream using callback (3)
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                stream_callback=callback)

# start the stream (4)
stream.start_stream()

#time.sleep(5)

# wait for stream to finish (5)
while stream.is_active():
        time.sleep(5)

# stop stream (6)
stream.stop_stream()
stream.close()
#wf.close()

# close PyAudio (7)
p.terminate()
