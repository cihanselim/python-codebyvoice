#!/usr/bin/env python3
import speech_recognition as sr
# from Tkinter import * (event handler is not ready yet)

listen = True
def callback(recognizer, audio):
    global listen
    try:
        if recognizer.recognize_google(audio).startswith("start"):
            print("Microphone started.")
            listen = True
        if listen:
            if not (recognizer.recognize_google(audio).startswith('start') or recognizer.recognize_google(
                    audio).startswith('stop')):
                print("SR thinks you said: " + recognizer.recognize_google(audio).upper())
            elif recognizer.recognize_google(audio).startswith('stop'):
                print("Microphone stopped.")
                listen = False
    except sr.UnknownValueError:
        print("waiting for a command...")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

r = sr.Recognizer()
r.energy_threshold = 4000
m = sr.Microphone()

with m as source:
    r.adjust_for_ambient_noise(source)

"""
we only need to calibrate once, before we start listening in the background (note that we don't have to
do this inside a `with` statement)
"""

stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations

import time

for _ in range(50):
    time.sleep(0.1)  # we're still listening even though the main thread is doing other things
"""
stop_listening() # calling this function requests that the background listener stop listening
"""
while True:
    time.sleep(0.0001)