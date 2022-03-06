# VIDEO CIPHERING

# Import libraries - tkinter, numpy, cv2, PIL, os, random and moviepy

import tkinter as tk
from tkinter import *
import tkinter.messagebox as mbox
from PIL import ImageTk, Image
import tkinter.messagebox as mbox
from tkinter import ttk
from tkinter import filedialog
import cv2
import numpy as np
import random
import os
from cv2 import *
from moviepy.editor import *


# Application Window & Configuration

window = tk.Tk() # created a tkinter gui window frame
window.title("Video Ciphering") # title for the window frame
window.geometry('1000x700') # window size


# Top label

start1 = tk.Label(text = "VIDEO  CIPHERING", font=("Arial", 55,"underline"), fg="black")
start1.place(x = 120, y = 10)


# Defining the start function
# The current window should be killed when user chooses START

def startFunction():
    window.destroy()


# START button created and assigned the functionality

startb = Button(window, text="START", command=startFunction, font=("Arial", 25), bg = "green", fg = "black", borderwidth=3, relief="raised")
startb.place(x = 150, y = 600 )


# Adding an image on the main window

path = "Images/front.jpg"


# Creates a Tkinter-compatible photo image from Images folder in local

img1 = ImageTk.PhotoImage(Image.open(path))


# Label widget to display an image on the screen

panel = tk.Label(window, image = img1)
panel.place(x = 130, y = 230)


# Defining the exit function
# When the user clicks on the exit button, it will ask the user if he/she wants to exit the application

def exitFunction():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
        
        
# EXIT button created and assigned the functionality

exitb = Button(window, text="EXIT",command=exit_win,font=("Arial", 25), bg = "red", fg = "white", borderwidth=3, relief="raised")
exitb.place(x =730 , y = 580 )
