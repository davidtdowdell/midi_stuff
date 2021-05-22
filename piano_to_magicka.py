
import mido
import pydirectinput as keyboard
import time, string


chars = string.ascii_lowercase+string.digits

keys = ['q', 'b', 'w', 'e', 'space', 'r', 'z', 'a', 's', 'c', 'd', 'x', 'f']




note2key = {47: "mouseLeft",
            48: "mouseDown",
            49: "mouseUp",
            50: "mouseRight"}

##for i in range(0, len(chars)):
##    octave = int(i/7)
##    step = i%7
##    num = 48+keys[step]+12*octave
##
##    note2key[num] = chars[i]

currNote = 69
for k in keys:
    note2key[currNote] = k
    currNote+=1

move=True
with mido.open_input() as inport:
    for msg in inport:
        if(msg.type is 'note_on'):
            print(msg)
            note = msg.note
            if note in note2key.keys():
                #If velocity >5. press key down
                key = note2key[note]
                if "mouse" not in key:
                    if msg.velocity > 5:
                        keyboard.keyDown(note2key[note], _pause=False)
                        if key == 'b':
                            move = False
                    else:
                        keyboard.keyUp(note2key[note], _pause=False)
                        if key == 'b':
                            move = True
                else:
                    if msg.velocity < 5:
                            keyboard.keyUp('m', _pause=False)
                    elif move:
                        keyboard.keyDown('m', _pause=False)
                    if msg.velocity > 5:
                        pos = keyboard.position()
                        if key == "mouseUp":
                            if pos[1] > 60:
                                keyboard.moveRel(yOffset=-50, _pause=False)
                        elif key == "mouseDown":
                            if pos[1] < 1024-60:
                                keyboard.moveRel(yOffset=50, _pause=False)
                        elif key == "mouseLeft":
                            if pos[0] > 60:
                                keyboard.moveRel(xOffset=-50, _pause=False)
                        elif key == "mouseRight":
                            if pos[0] < 1280-60:
                                keyboard.moveRel(xOffset=50, _pause=False)
                        elif key == "mouseRight":
                            if pos[0] < 1280-60:
                                keyboard.moveRel(xOffset=50, _pause=False)
                        elif key == "mouseRC":
                            keyboard.keyUp('m', _pause=False)
                            keyboard.rightClick(_pause=False)
                            move=False
                    elif 'C' in key:
                        move=True

                        
            #else:
                #print(note, 'NOT REGISTERED')
    
    
        #11666qqqhbcdefgopjklmnvwxrstu2hhbabbcdefghijklmnopqrstuvwxyz0121111aa11abcdefghihjklmnopqrstuvwxyz01234566
