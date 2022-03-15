import os
from os.path import splitext
import pydub
from pydub import AudioSegment


def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then return output_file '''
    
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = 'Compressed_' + input_filename + '.mp3'
    output_file = os.path.join(output_path, output_filename)
    
    # Fetch the file 
    compressed = pydub.AudioSegment.from_file(input_file)
    
    # Save the compressed file
    compressed.export(output_file, format = "wav")

    return output_file