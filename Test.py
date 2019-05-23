#from tkinter import *
#import tkinter.font
import time
#from gpiozero import LED
#import RPi.GPIO as i0



#io.setmode(io.BOARD)
#window = Tk()
#window.title("Morse code")
#myFont= tkinter.font.Font(family = 'Helvetica', size = 12)
#morse= ""
#led= LED(16)

word = input("Enter:")
#word.upper()
String = list(word.upper())
print(String)

Letters =['A#.,-','B#-,.,.,.', 
                    'C#-,.,-,.', 'D#-,.,.', 'E#.', 
                    'F#.,-,.', 'G#-,-,.', 'H#.,.,.,.', 
                    'I#.,.', 'J#.,-,-,-', 'K#,-,.,-', 
                    'L#.,-,.,.', 'M#-,-', 'N#-,.', 
                    'O#-,-,-', 'P#.,-,-,.', 'Q#-,-,.,-', 
                    'R#.,-,.', 'S#.,.,.', 'T#-', 
                    'U#.,.,-', 'V#.,.,.,-', 'W#.,-,-', 
                    'X#-,.,.,-', 'Y#-,.,-,-', 'Z#-,-,.,.', 
                    '1#.,-,-,-,-', '2#.,.,-,-,-', '3#.,.,.,-,-', 
                    '4#.,.,.,.,-', '5#.,.,.,.,.', '6#-,.,.,.,.', 
                    '7#-,-,.,.,.', '8#-,-,-,.,.', '9#-,-,-,-,.', 
                    '0#-,-,-,-,-', ',#-,-,.,.,-,-', '.#.,-,.,-,.,-', 
                    '?#.,.,-,-,.,.', '/#-,.,.,-,.', '-#-,.,.,.,.,-', 
                    '(#-,.,-,-,.', ')#-,.,-,-,.,-']

#def longBlink():
 #   led.on()
  #  time.sleep(1000)
   # led.off()
#def shortBlink():
#    led.on()
#    time.sleep(2000)
#   led.off()

#def main():
for i in range(len(String)):
    for j in range(len(Letters)):
        character = Letters[j].split("#")
        #print(character[1])
        if String[i] == character[0] :
            sign = character[1]
            signlist = sign.split(",")
            print(character[0])
            #print(signlist)
            for x in range(len(signlist)):
                if (signlist[x] == '-'):
                        #longBlink()
                    
                    print("Long")
                else:
                        #shortBlink()
                    print("Short")
                    

    
