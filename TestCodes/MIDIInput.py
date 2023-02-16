# python3 -m pip install mido

# pip3 install py-midi

import mido

with mido.open_input() as inport:
    for msg in inport:
        if (msg.type == 'note_on'):
            print(msg)
            print(msg.note)
