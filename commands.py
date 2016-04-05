#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import speech_recognition as sr
import ScrolledText
from Tkinter import *
import tkFileDialog
import tkMessageBox

def stopKey(event):
    global listen
    listen = False
    print "Microphone has stopped."

def startKey(event):
    global listen
    listen = True
    print "Microphone has started."

def ifStatement():
    textPad.insert(INSERT, "if (): \n\t #if statement here\nelif (): \n\t #if statement here \nelse: \n\t #else statement here")

def lowerThan():
    textPad.insert(INSERT, " < ")

def newLine():
    textPad.insert(INSERT, "\n")

def randomNum():
    textPad.insert(INSERT, "deneme = random.randint(1,10)")

def space():
    textPad.insert(INSERT, " ")

def printL(recognizer, audio):
    textPad.insert(INSERT, "print \"%s\"" % (INSERT))

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


root = Tk()
textPad = ScrolledText.ScrolledText(root, width=70, height=30, font=("Arial", 14, "normal"))
