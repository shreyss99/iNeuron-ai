from pylovepdf.ilovepdf import ILovePdf
import os
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
    public_key = 'Your public key here'
    
    # Creating a ILovePdf object
    ilovepdf = ILovePdf(public_key, verify_ssl=True)
    
    # Assigning a new compress task
    task = ilovepdf.new_task('compress')
    
    # Adding the input pdf file and setting output directory
    task.add_file(input_file)
    task.set_output_folder(output_path)
    
    # Execute the compression task
    task.execute()

    # Download the compressed file
    task.download()
    
    pattern = output_path + "*.pdf"
    result = glob.glob(pattern)
    
    for file_name in result:
        old_name = file_name
        new_name = output_file
        os.rename(old_name, new_name)
    
    return output_file