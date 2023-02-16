import mido
import pyautogui as pg

def MIDItochar(inputNum):
    outputChar = " "
    # numbers 0-9
    if (inputNum >= 48 and inputNum < 58):
        outputChar = chr(inputNum)
    # SPACE
    elif(inputNum == 58):
        outputChar = chr(32)
    # backspace
    elif(inputNum == 59):
        outputChar = "backspace"
    # lower case chars
    elif(inputNum >= 60 and inputNum < 86):
        outputChar = chr(inputNum + 37)
    
    # print(outputChar)
    return outputChar

def MIDItoStroke(note):
    pg.typewrite([MIDItochar(note)])


    

with mido.open_input() as inport:
    for msg in inport:
        if (msg.type == 'note_on'):
            # print(msg.note)
            MIDItoStroke(msg.note)
"""
TODO

1. use chord as dictionary or create hot keys for vsts

2. add a note to start and stop typing, use bool
"""


