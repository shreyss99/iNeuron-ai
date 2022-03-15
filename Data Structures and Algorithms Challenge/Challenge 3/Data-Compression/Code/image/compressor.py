import PIL
from PIL import Image
import os

def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then return output_file '''
    
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = 'Compressed_IMAGE_' + input_filename + '.png'
    output_file = os.path.join(output_path, output_filename)
    
    # Open image and get its dimensions
    image = Image.open(input_file)
    height, width = image.size
    
    # Using resize option and ANTIALIAS to compress the image and reduce jerkyness
    compressed_image = image.resize((height,width), Image.ANTIALIAS)
    
    # Save compressed image at the output path
    save_compressed_file = compressed_image.save(output_filename, quality=100, optimize=True) 
    
    return output_file