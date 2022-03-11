## VIDEO CIPHERING
-  This is a Video Ciphering application created in python with tkinter gui and OpenCV library.
-  In this application user can select any video (either mpy, mp4, avi, or any other extension of video) and will be able to encrypt, decrypt and reset the encrypted video to original format.
-  Along with encryption, decryption, user will also be able to see the preview of encrypted, decrypted and original video.

***

### Requirements:
- python 3
- tkinter module
- filedialog from tkinter
- messagebox
- from PIL import Image, ImageTk
- cv2
- numpy
- os
- random
- moviepy

****

### How to use it:
- For simplicity, the executable Python code is placed in the 'Code' folder. For running locally, ensure that the code file is in the same path as the 'Images' folder.
- User needs to install tkinter, PIL, cv2, numpy, os, random, moviepy.
- Ensure that the local environment does not have both Pillow and PIL as it will not work.
	- If that is the case first remove PIL using: 
	```pip uninstall PIL```
	- Afterwards, install the Pillow library using: 
	```pip install Pillow```
	
- User need to download the code, and run the Video_Ciphering.py, on local system.
- After running a GUI window appears, where user can start the video ciphering application by clicking on the START button.
- After that a new GUI window will open, in which user will have buttons like SELECT, ENCRYPT VIDEO, DECRYPT VIDEO, RESET and EXIT.
- Firstly, the user has to select any video file (either mpy, mkv, avi, or any other extension of video) from the local system, using SELECT button.
- After selecting the file, user will be able to see the path of the video selected in the text area.
- The user can now click on the ENCRYPT VIDEO button and the encryption process will start and user will be shown an encrypted video as a preview.
- After that user can decrypt the encrypted video, using DECRYPT VIDEO which will show decrypted video as a preview.
- Also there is a RESET button which can reset the video to original format and will show the preview for the same.
- The EXIT button allows which user to exit from the application.

***