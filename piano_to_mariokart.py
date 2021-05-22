
import mido
import pydirectinput as keyboard
import time, string


chars = string.ascii_lowercase+string.digits

keys = [0, 2, 4, 5, 7, 9, 11]




note2key = {}

for i in range(0, len(chars)):
    octave = int(i/7)
    step = i%7
    num = 48+keys[step]+12*octave

    note2key[num] = chars[i]

with mido.open_input() as inport:
    for msg in inport:
        if(msg.type is 'note_on'):
            print(msg)
            note = msg.note
            if note in note2key.keys():
                #If velocity >5. press key down
                if msg.velocity > 5:
                    keyboard.keyDown(note2key[note], _pause=False)
                else:
                    keyboard.keyUp(note2key[note], _pause=False)
                    
            #else:
                #print(note, 'NOT REGISTERED')
    
    
        #11666qqqhbcdefgopjklmnvwxrstu2hhbabbcdefghijklmnopqrstuvwxyz0121111aa11abcdefghihjklmnopqrstuvwxyz01234566
