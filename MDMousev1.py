import mido
import pyautogui as pg


def MIDItoMouse(note):
    match note:
        case 36:
            pg.mouseDown()
        case 37:
            pg.mouseDown(button='right')
        case 38:
            pg.mouseUp()
        case 39:
            pg.mouseUp(button='right')
        case 40:
            pg.click()
        # scroll up
        case 41:
            pg.scroll(10)
        # scroll down
        case 43:
            pg.scroll(-10)
        # move up
        case 44:
            pg.move(0, -50)
        # move down
        case 45:
            pg.move(0, 50)
        # move left
        case 46:
            pg.move(-50, 0)
        # move right
        case 47:
            pg.move(50, 0)
        


with mido.open_input() as inport:
    for msg in inport:
        if (msg.type == 'note_on'):
            print(msg.note)
            MIDItoMouse(msg.note)