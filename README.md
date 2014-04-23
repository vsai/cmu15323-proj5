15-323 Computer Music Systems and Information Processing
Spring 2014
Project 5 - Self-designed project


Description:
This project involves construction of computer musical sounds using vocal inputs. How it works is that it reads
input stream data from the mic, and calculates the note of what you are singing (based on the resonant frequency,
which was determined by using FFTs) and sends the note over to the server.

The server would then play the MIDI note using an instrument. The instrument that is used is determined by controls
via an external OSC client (TouchOSC). The server would then play the note in real-time, and you could modify the
instrument with a buttonclick on the OSC client.

Next stages:
- Chord Mode: Have an option which would allow you to play the chord associated with the particular note (play C4-E4-G4 on 
receiving the note C4)
- (Stretch goal): Tempo detection option allowing you to set the BPM by tapping a surface near the mic


Install:
pyaudio (pip install pyaudio)
numpy (pip install numpy)
wave (pre-installed)

To Run:
python streams_freqdetect.py

To exit:
Ctrl-C
