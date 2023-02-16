import mido
import pyautogui as pg


def MIDItoMouse(note):
    match note:
        case 48:
            pg.mouseDown()
        case 49:
            pg.mouseDown(button='right')
        case 50:
            pg.mouseUp()
        case 51:
            pg.mouseUp(button='right')
        case 52:
            pg.click()
        # scroll up
        case 53:
            pg.scroll(10)
        # scroll down
        case 53:
            pg.scroll(-10)
        # move up
        case 60:
            pg.move(0, -50)
        # move down
        case 62:
            pg.move(0, 50)
        # move left
        case 64:
            pg.move(-50, 0)
        # move right
        case 65:
            pg.move(50, 0)
        


with mido.open_input() as inport:
    for msg in inport:
        if (msg.type == 'note_on'):
            print(msg.note)
            MIDItoMouse(msg.note)