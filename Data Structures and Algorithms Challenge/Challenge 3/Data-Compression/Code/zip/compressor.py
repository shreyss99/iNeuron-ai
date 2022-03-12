import zipfile
import io
import os

def compress(input_file, output_path):

    # Compress input_file, store it in output_path and then return output_file
    # Get file name and extension
    
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    