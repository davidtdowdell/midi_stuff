
import mido
import pydirectinput as keyboard
import time









note2key = {38:     '4',    # B button
            40:     '4',    # B button
            46:     'q',     # Shake
            42:     'q',     # Shake
            44:     'u',     # Item
            49:     '6',    # Left
            48:     '7',    # Up
            45:     '8',    # Down
            43:     '9',    # Plus
            51:     '0',    # Right
            36:     '1',    # A button
    }
keyTime = { 38:     100,    # Snare
            40:     100,    # Rim
            46:     100,    # Open HiHat
            42:     100,    # Closed HiHat114uuuu77614uu1u17
            44:     100,    # Closing HiHat
            49:     100,    # Crash Cymbal
            48:     100,    # Left Tom
            45:     100,    # Middle Tom
            43:     100,    # Right Tom
            51:     100,    # Ride Cymbal
            36:     1000     # Bass Drum
    }

    


pressed = {}
downTimeStart = {}

for i in note2key.keys():
    pressed[i] = False
    downTimeStart[i] = 0.0

with mido.open_input() as inport:
    for msg in inport:
        if(msg.type == 'note_on' and msg.velocity>5):
            #print(msg)
            note = msg.note
            if note in note2key.keys():
                #If key is pressed, reset timer
                if pressed[note]:
                    downTimeStart[note] = time.time()
                    
                #If key is not pressed, press and start timer
                else:
                    keyboard.keyDown(note2key[note])
                    pressed[note] = True
                    downTimeStart[note] = time.time()
                    print(str(note) + " down")
            else:
                print(note, 'NOT REGISTERED')

        #At every message, check timers
        for note in note2key.keys():
            if pressed[note]:
                downTime = time.time() - downTimeStart[note]
                if downTime*1000 > keyTime[note]:
                    keyboard.keyUp(note2key[note])
                    pressed[note] = False
                    print(str(note) + " up")
    
    
        #11666qqq
