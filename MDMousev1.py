import mido
import pyautogui as pg


def MIDItoMouse(note):
    match note.note:
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
            pg.scroll(note.velocity / 20)
        # scroll down
        case 43:
            pg.scroll(note.velocity / -20)
        # move up
        case 44:
            pg.move(0, note.velocity / -3)
        # move down
        case 45:
            pg.move(0, note.velocity / 3)
        # move left
        case 46:
            pg.move(note.velocity / -3, 0)
        # move right
        case 47:
            pg.move(note.velocity / 3, 0)
        


with mido.open_input() as inport:
    for msg in inport:
        if (msg.type == 'note_on'):
            print(msg.velocity)
            MIDItoMouse(msg)