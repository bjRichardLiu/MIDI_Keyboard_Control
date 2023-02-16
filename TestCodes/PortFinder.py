import time
# pip3 install git+https://github.com/SpotlightKid/python-rtmidi.git@eb16ab3268b29b94cd2baa6bfc777f5cf5f908ba#egg=python-rtmidi
import rtmidi

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)