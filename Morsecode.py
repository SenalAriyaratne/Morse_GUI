
# to do this task I reffered to the Morse code converter guide. The link to that guide is given below.
# Link : https://www.geeksforgeeks.org/morse-code-translator-python/
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)


led = LED(4)

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'}



window = Tk()
window.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

def longblink():
    led.on()
    time.sleep(1)
    led.off()
def shortblink():
    led.on()
    time.sleep(0.5)
    led.off()
    
def encrypt(message): 
    cipher = '' 
    for letter in message.upper(): 
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher

    
def main():
    for element in encrypt(userinput.get()):
        if element == " ":
            time.sleep(1)
        if element == ".":
            shortblink()
            time.sleep(1)
        if element == "-":
            longblink()
            time.sleep(1)
            


def close():
    RPi.GPIO.cleanup()
    window.destroy()



userinput = Entry(window, width=12)
userinput.grid(row=1, column=1)

submit = Button(window, text='Submit', font=myFont, command=main, bg='bisque2', height=1, width=3)
submit.grid(row=1, column=2)

Exit = Button(window, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
Exit.grid(row=2, column=1)

window.protocol("WM_DELETE_WINDOW", close) 

window.mainloop() 


 


    
