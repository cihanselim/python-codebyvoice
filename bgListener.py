#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import speech_recognition as sr
import ScrolledText
from Tkinter import *
from commands import *

listen = True
def callback(recognizer, audio):
    global listen
    try:
        if listen:
            list = [u"kontrol",u"alta geç",u"rastgele sayı",u"küçüktür",u"boşluk",u"yazdır"]

            if recognizer.recognize_google(audio, language="tr") not in list:
                textPad.insert(INSERT, recognizer.recognize_google(audio, language="tr"))

            else:
                if recognizer.recognize_google(audio, language="tr") == u"kontrol":
                     ifStatement()

                elif recognizer.recognize_google(audio, language="tr") == u"rastgele sayı":
                     randomNum()

                elif recognizer.recognize_google(audio, language="tr") == u"yazdır":
                     printL(recognizer, audio)

                elif recognizer.recognize_google(audio, language="tr") == u"alta geç":
                     newLine()

                elif recognizer.recognize_google(audio, language="tr") == u"küçüktür":
                     lowerThan()

                elif recognizer.recognize_google(audio,language="tr") == u"boşluk":
                     space()
        else:
            listen = False
    except sr.UnknownValueError:
        print("waiting for a command...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
r.energy_threshold = 800
r.pause_threshold = 0.5
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

stop_listening = r.listen_in_background(m, callback)

#Tkinter starts here

#Editor menus here
menu = Menu(root)
root.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
# filemenu.add_command(label="New")
filemenu.add_command(label="Open...", command=open_command)
filemenu.add_command(label="Save", command=save_command)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command)
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about_command)
textPad.pack()
root.mainloop()

root.resizable(False,True) #editor enine buyumez, boyuna buyur
root.wm_protocol("WM_DELETE_WINDOW", Tk) #kapatmayi engeller
textPad.quit()
root.wm_attributes("-alpha", 0.9) #opacity
textPad.bind('<F12>', stopKey)
textPad.bind('<F11>', startKey)

import time
for _ in range(50):
    time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening() # calling this function requests that the background listener stop listening
while True:
    time.sleep(0.1)