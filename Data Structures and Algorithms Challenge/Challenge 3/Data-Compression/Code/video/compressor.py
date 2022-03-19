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