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

startFirst = tk.Label(text = "VIDEO  CIPHERING", font = ("Arial", 55,"underline"), fg = "black")
startFirst.place(x = 120, y = 10)


# Defining the start function
# The current window should be killed when user chooses START

def startFunction():
    window.destroy()


# START button created and assigned the functionality

startButton = Button(window, text = "START", command = startFunction, font = ("Arial", 25), bg = "green", fg = "black", borderwidth = 3, relief = "raised")
startButton.place(x = 150, y = 600)


# Adding an image on the main window

path = "Images/front.jpg"


# Creates a Tkinter-compatible photo image from Images folder in local

imageBackground = ImageTk.PhotoImage(Image.open(path))


# Label widget to display an image on the screen

panel = tk.Label(window, image = imageBackground)
panel.place(x = 130, y = 230)


# Defining the exit function
# When the user clicks on the exit button, it will ask the user if he/she wants to exit the application

def exitFunction():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
        
        
# EXIT button created and assigned the functionality

exitb = Button(window, text = "EXIT", command = exitFunction, font = ("Arial", 25), bg = "red", fg = "white", borderwidth = 3, relief = "raised")
exitb.place(x = 730 , y = 580)


# Call exit function when the button is pressed

window.protocol("WM_DELETE_WINDOW", exitFunction)
window.mainloop()


# Main Window & Configuration once START Button is presses

windowNew = tk.Tk() # created a tkinter gui window frame
windowNew.title("Video Ciphering") # title for the window frame
windowNew.geometry('1000x700') # window size


# Function to allow user to select input file

def openFile():
    global filename
    filename = filedialog.askopenfilename(title="Select file")
    path_text.delete("1.0", tk.END) # Remove the box for choosing file once file is selected
    path_text.insert(END, filename) # Add the filename


# Function to encrypt video and show encrypted video
def encryptFunction():
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
        
    # Set variables    
    currentframe = 0
    count = 0
    
    while (True):
    
        # Read from frame by accessing webcam
        ret, frame = cam.read() # ret stores boolean if frame is read correctly and frame stores the frame
        
        if ret:
            if currentframe % fps == 0:
            
                # If video is still left continue creating images
                suffix = currentframe // fps
                name = './Sample_Output/frame' + str(suffix) + '.jpg'

                count += 1

                # Write the extracted images
                cv2.imwrite(name, frame)


                # Convert to encrypted image
                #-------------------------------------------------------
                
                # Change image to gray scale
                image_input = cv2.imread(name, cv2.IMREAD_GRAYSCALE)
                
                # Calculate image frame shape
                (image_rows, image_cols) = image_input.shape
                
                # Convert the image into an array of floats and divide value by 255 to standardise
                image_input = image_input.astype(float) / 255.0
                
                mu, sigma = 0, 0.04  # mean and standard deviation
                
                # Generate a key by using randomly initialised array and adding epsilon limits for nore randomisation
                encryptionKey = np.random.normal(mu, sigma, (image_rows, image_cols)) + np.finfo(float).eps
        
                # Get encrypted image and storing it
                image_encrypted = image_input / encryptionKey
                nameEncrypted = './Sample_Output/encrypted' + str(suffix) + '.jpg'
                cv2.imwrite(nameEncrypted, image_encrypted * 255)
                
                # ----------------------------------------------------------
            
             currentframe += 1
        else:
            break
 

    cam.release()
    cv2.destroyAllWindows()
    
    # Capture encrypted video
    
    ic_list = []
    for i in range(count):
        ic_list.append(ImageClip("Images/sample.jpg").set_duration(1))
    video = concatenate(ic_list, method="compose")
    video.write_videofile('Output_Video.mp4', fps=fps)  
    
    # Play encrypted video ------------
    
    cap = cv2.VideoCapture('Output_Video.mp4')
    
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    # Read until video is completed
    while(cap.isOpened()):
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

            # Display the resulting frame
            cv2.imshow('Encrypted Video', frame)

            # Press Q on keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    
# Function to decrypt video and show decrypted video

def decryptFunction():

    global filename
    cap = cv2.VideoCapture(filename)
    
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    
    while(cap.isOpened()):
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:
        
            # Converting to gray scale
            grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Display the resulting frame
            cv2.imshow('Decrypted Video', grayImage)

            # Press Q on keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    
def resetFunction():
    global filename
    cap = cv2.VideoCapture(filename)
    
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")
    
    while(cap.isOpened()):
    
        # Capture frame-by-frame
        ret, frame = cap.read()
        if ret == True:

        # Display the resulting frame
            cv2.imshow('Original Video', frame)

        # Press Q on keyboard to exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
    cap.release()
    cv2.destroyAllWindows()
    
    

# Top label configuratio

startFirst = tk.Label(text = "VIDEO  CIPHERING", font = ("Arial", 55, "underline"), fg = "black")
startFirst.place(x = 120, y = 10)

lbl2 = tk.Label(text="Selected Video", font=("Arial", 30),fg="brown")
lbl2.place(x = 80, y = 220)

# Selection box

path_text = tk.Text(windowNew, height = 3, width = 37, font = ("Arial", 30), bg = "light yellow", fg = "orange", borderwidth = 2, relief = "solid")
path_text.place(x = 80, y = 270)


# Select Button with Encryption function

selectb=Button(windowNew, text = "ENCRYPT VIDEO", command = encryptFunction, font = ("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 120, y = 450)


# Select Button with Decryption function

selectb=Button(windowNew, text = "DECRYPT VIDEO", command = decryptFunction, font = ("Arial", 25), bg = "orange", fg = "blue")
selectb.place(x = 550, y = 450)


# Select Button to Open File

selectb=Button(windowNew, text = "SELECT", command = openFile, font = ("Arial", 25), bg = "light green", fg = "blue")
selectb.place(x = 80, y = 580)


# Select Button with Reset function

getb=Button(windowNew, text = "RESET", command = resetFunction, font = ("Arial", 25), bg = "yellow", fg = "blue")
getb.place(x = 420, y = 580)


# Option for exit of window

def exitWindowNew():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        windowNew.destroy()
        

# Exit Button

getb=Button(windowNew, text = "EXIT", command = exitWindowNew, font = ("Arial", 25), bg = "red", fg = "blue")
getb.place(x = 780, y = 580)

windowNew.protocol("WM_DELETE_WINDOW", exitWindowNew)
windowNew.mainloop()

