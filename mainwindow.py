#!/usr/bin/env python

from tkinter import *
import tkinter.messagebox as tkMessageBox

mainwindow = Tk()

label = Label(mainwindow, text="Labyrinth")
label.pack()

quitbutton = Button(mainwindow, text="quit", command= mainwindow.quit)
quitbutton.pack()

Canvas(mainwindow, width=250, height=50, bg='ivory').pack(side=LEFT, padx=5, pady=5)
Button(mainwindow, text ='Bouton 1').pack(side=TOP, padx=5, pady=5)
Button(mainwindow, text ='Bouton 2').pack(side=BOTTOM, padx=5, pady=5)

mainwindow.mainloop()



