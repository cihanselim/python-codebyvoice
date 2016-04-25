#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import ScrolledText
import speech_recognition as sr

from Tkinter import *
import tkFileDialog
import tkMessageBox

def ifStatement():
    textPad.insert(INSERT, "if (): \t #if statement here\nelif (): \t "
                           "#if statement here \nelse: \t #else statement here")

def forLoop():
    textPad.insert(INSERT, "for i in range():")

def equal():
    textPad.insert(INSERT, "= ")

def doubleEqual():
    textPad.insert(INSERT, "== ")

def lessThan():
    textPad.insert(INSERT, "< ")

def greaterThan():
    textPad.insert(INSERT, "> ")

def bigEqual():
    textPad.insert(INSERT, ">= ")

def lowEqual():
    textPad.insert(INSERT, "<= ")

def newLine():
    textPad.insert(INSERT, "\n")

def randomNum():
    textPad.insert(INSERT, "deneme = random.randint(1,10)")

def getSpace():
    textPad.insert(INSERT, " ")

def getTab():
    textPad.insert(INSERT, "\t")

def getPrint():
    textPad.insert(INSERT, "print \"\"" )

def standard_write(string):
    textPad.insert(INSERT, string)
    getSpace()
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
textPad = ScrolledText.ScrolledText(root, width=100, height=40, font=("Consolas", 12, "normal"))
textPad.config(background="#282828",foreground ="white",insertbackground="white")
