#!/usr/bin/env python3
import speech_recognition as sr
import ScrolledText
from Tkinter import *

def stopKey(event):
    global listen
    listen = False
    print "Microphone has stopped."

def startKey(event):
    global listen
    listen = True
    print "Microphone has started."

# def forLoop(event):
#     a = "for i in range():\n\tx=1\n\tprint x"
#     textPad.insert(END, a)

listen = True
def callback(recognizer, audio):
    global listen

    try:
        if listen:
            textPad.insert(END, recognizer.recognize_google(audio))
            # if recognizer.recognize_google(audio) == "tap":
            #     textPad.insert(END, " ")
            print("--> " + recognizer.recognize_google(audio).upper())
        else:
            listen = False
    except sr.UnknownValueError:
        print("waiting for a command...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
r.energy_threshold = 4000
r.pause_threshold = 0.5
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

#Tkinter starts here
root = Tk()
textPad = ScrolledText.ScrolledText(root, width=80, height=40, font=("Source Sans Pro", 14, "normal"), bg="#F7F7F7")
textPad.quit()
root.wm_attributes("-alpha", 0.9) #opacity
textPad.bind('<F12>', stopKey)
textPad.bind('<F11>', startKey)
# textPad.bind('<F1>', forLoop)
root.resizable(False,True) #enine buyumez, boyuna buyur
root.wm_protocol("WM_DELETE_WINDOW", Tk) #kapatmayi engeller
textPad.pack()
root.mainloop()

import time
for _ in range(50):
    time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening() # calling this function requests that the background listener stop listening
while True:
    time.sleep(0.1)