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

startb = Button(window, text="START",command=start_fun,font=("Arial", 25), bg = "green", fg = "black", borderwidth=3, relief="raised")
startb.place(x = 150, y = 600 )


# Adding an image on the main window

path = "Images/front.jpg"



