from pylovepdf.ilovepdf import ILovePdf
import os
import pathlib
import glob

# public key
global public_key


def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then return output_file '''
    
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = 'Compressed_' + input_filename + '.pdf'
    output_file = os.path.join(output_path, output_filename)
    
    ''' We are using ilovepdf API for compression. So need a public-key to use this module, 
    for that login on to https://developer.ilovepdf.com/ 
    and public key will be visible in the ‘My Projects’ section '''
    public_key = 'Your public key'
    
    # creating a ILovePdf object
    ilovepdf = ILovePdf(public_key, verify_ssl=True)
    
    # assigning a new compress task
    task = ilovepdf.new_task('compress')