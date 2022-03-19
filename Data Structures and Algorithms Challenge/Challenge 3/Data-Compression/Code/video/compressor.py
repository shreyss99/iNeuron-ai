import cv2
import sys
import os


def compress(input_file, output_path):
'''Get input file name and extension'''
    
    # Get input file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = 'Compressed_' + input_filename + '.mp4'
    output_file = os.path.join(output_path, output_filename)
 
    # Getting video and then processing it and saving it
    cap = cv2.VideoCapture(input_file)

    compression_value = 50
    width  = cap.get(3) * compression_value / 100
    height = cap.get(4) * compression_value / 100
    
    out_video = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'mp4v'), 20.0, (int(width), int(height)), True)
    
    # Write each frame from the video into output video
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            frameX = rescale_frame(frame, compression_value)
            out_video.write(frameX) 
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
            
# Resizing all frames
def rescale_frame(frame, percent):
    width = int(frame.shape[1] * percent / 100)
    height = int(frame.shape[0] * percent / 100)
    dimensions = (width, height)
    return cv2.resize(frame, dimensions)