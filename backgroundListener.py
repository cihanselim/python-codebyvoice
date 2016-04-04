#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
import ScrolledText
from Tkinter import *
import tkFileDialog
import tkMessageBox
# from commands import *
def stopKey(event):
    global listen
    listen = False
    print "Microphone has stopped."

def startKey(event):
    global listen
    listen = True
    print "Microphone has started."

def forLoop():
    textPad.insert(INSERT, "for i in range():")

def ifStatement():
    textPad.insert(INSERT, "if (): \n\t #if statement here\nelif (): \n\t #if statement here \nelse: \n\t #else statement here")

def lowerThan():
    textPad.insert(INSERT, " < ")

def lowerEqualThan():
    textPad.insert(INSERT, " <= ")

def biggerThan():
    textPad.insert(INSERT, " > ")

def biggerEqualThan():
    textPad.insert(INSERT, " >= ")

def EqualEqual():
    textPad.insert(INSERT, " == ")

def Equal():
    textPad.insert(INSERT, " = ")

def newLine():
    textPad.insert(INSERT, "\n")

def input():
    textPad.insert(INSERT, "deneme = int(raw_input('Bir sayı giriniz: '))")

def randomNum():
    textPad.insert(INSERT, "deneme = random.randint(1,10)")

def open_command():
        file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.insert('1.0',contents)
            file.close()

def save_command():
    file = tkFileDialog.asksaveasfile(mode='w')
    if file != None:
    # slice off the last character from get, as an extra return is added
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()

def about_command():
    label = tkMessageBox.showinfo("About", "Code by Voice\nCihan SELİM")

def exit_command():
    if tkMessageBox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()

listen = True
def callback(recognizer, audio):
    global listen

    try:
        if listen:
            list = [u"kontrol",u"alta geç",u"rastgele sayı",u"küçüktür"]

            if recognizer.recognize_google(audio, language="tr") not in list:
                textPad.insert(INSERT, recognizer.recognize_google(audio, language="tr"))

            if recognizer.recognize_google(audio, language="tr") == u"kontrol":
                 ifStatement()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"input ekle":
            #      input()

            elif recognizer.recognize_google(audio, language="tr") == u"rastgele sayı":
                 randomNum()

            elif recognizer.recognize_google(audio, language="tr") == u"alta geç":
                 newLine()

            elif recognizer.recognize_google(audio, language="tr") == u"küçüktür":
                 lowerThan()

            # elif recognizer.recognize_google(audio, language="tr") == u"küçük eşittir":
            #      lowerEqualThan()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"büyüktür":
            #      biggerThan()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"büyük eşittir":
            #      biggerEqualThan()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"eşitse":
            #      EqualEqual()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"eşittir":
            #      Equal()
            #
            # elif recognizer.recognize_google(audio, language="tr") == u"yorum":
            #      newLine()

            else:
                pass

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
root = Tk()
textPad = ScrolledText.ScrolledText(root, width=70, height=30, font=("Arial", 14, "normal"))
textPad.quit()
root.wm_attributes("-alpha", 0.9) #opacity
textPad.bind('<F12>', stopKey)
textPad.bind('<F11>', startKey)
# textPad.bind('<F1>', forLoop)
root.resizable(False,True) #enine buyumez, boyuna buyur
root.wm_protocol("WM_DELETE_WINDOW", Tk) #kapatmayi engeller

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

import time
for _ in range(50):
    time.sleep(0.1)  # we're still listening even though the main thread is doing other things
# stop_listening() # calling this function requests that the background listener stop listening
while True:
    time.sleep(0.1)