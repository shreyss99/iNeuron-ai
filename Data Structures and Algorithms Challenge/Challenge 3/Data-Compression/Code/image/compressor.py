import PIL
from PIL import Image
import glob
import os

def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then return output_file '''
    
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = "Compressed_" + input_filename + '.png'
    output_file = os.path.join(output_path, output_filename)