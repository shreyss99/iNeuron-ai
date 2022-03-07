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
startb.place(x = 150, y = 600)


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

exitb = Button(window, text="EXIT", command=exitFunction, font=("Arial", 25), bg = "red", fg = "white", borderwidth=3, relief="raised")
exitb.place(x = 730 , y = 580)


# Call exit function when the button is pressed

window.protocol("WM_DELETE_WINDOW", exitFunction)
window.mainloop()


# Main Window & Configuration once START Button is presses

window1 = tk.Tk() # created a tkinter gui window frame
window1.title("Video Ciphering") # title for the window frame
window1.geometry('1000x700') # window size


# Function to allow user to select input file

def open_file():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    path_text.delete("1.0", tk.END) # Remove the box for choosing file once file is selected
    path_text.insert(END, filename) # Add the filename


# Function to encrypt video and show encrypted video
def encrypt_fun():
    global filename
    path_list = []

    # converting videos to images
    # ---------------------------------------------
    # Read the video from specified path
    cam = cv2.VideoCapture(filename)
    # Fetch the frames per second of the video
    fps = int(cam.get(cv2.CAP_PROP_FPS))
    
try:
    # Try creating a folder named 'Sample_Output' else raise Exception
    if not os.path.exists('Sample_Output'):
        os.makedirs('Sample_Output')

    except OSError:
        print('Error: Creating directory of data')




