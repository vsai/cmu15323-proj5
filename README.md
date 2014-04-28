15-323 Computer Music Systems and Information Processing
Spring 2014
Project 5 - Self-designed project


Description:
This project involves construction of computer musical sounds using vocal inputs. How it works is that it reads
input stream data from the mic, and calculates the note of what you are singing (based on the resonant frequency,
which was determined by using FFTs) and sends the note over to the server.

The server would then play the MIDI note using an instrument. The instrument that is used is determined by controls
via an external OSC client (TouchOSC). The server would then play the note in real-time.

Performance:
Our performance was 2-pronged
1. We played some famous tunes (Star Wars theme) 
2. We opened two channels together, Rishabh sang the music for All of Me (by John Legend) on the Organ channel (Channel 0), while Vishalsai spoke the "I have a dream" speech by Martin Luther King, Jr. into the Xylophone channel (Channel 1)


Install:
wxserpent64
pyaudio (pip install pyaudio)
numpy (pip install numpy)
wave (pre-installed)


To Run:
1. Server side -> cd into server directory where "init.srp" is present, and type the command "wxserpent64 init.srp". Server uses port 7770

2. Clients (1 and 2, both not required):
cd into main directory and type 
"python stream_freqdetect.py". Enter the following information
a. IP Address (of server)
b. MIDI Channel number (1 or 2, 1 => Organ 2 => Xylophone)
3. Confidence Interval (1 for ornamental sound, 2 or 3 for more rigid sound input)

3. Open your TouchOSC interface and 'cd' into your server's IP address. Then, on tab 1, toggle1 holds the play / mute button for Channel0 and toggle2 the same for Channel1.

To exit:
Ctrl-C on server (creates error on client side)
If you don't mute the sounds first, the midi note plays indefinitely. Hence, to fix this you could either mute before you end, or close SimpleSynth or your synth driver after you close the server.
