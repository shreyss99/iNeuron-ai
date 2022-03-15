import zipfile
import io
import os

def compress(input_file, output_path):

    # Compress input_file, store it in output_path and then return output_file
    
    # Get file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Output file name and path
    output_filename = 'Compressed_ZIP_' + input_filename + '.zip'
    output_file = os.path.join(output_path, output_filename)
    
    # Add compression type to DEFLATED
    compression_type = zipfile.ZIP_DEFLATED
    
    # Create a zipfile with write permission
    zf = zipfile.ZipFile(output_file, mode="w")
    
    try:
        # Compress the input file using zip and store file
        zip_file = zf.write(input_file, compress_type=compression_type)

    except FileNotFoundError as e:
        print(f'Exception occurred during zip process - {e}')
        
    finally:
        zf.close()
        
    return output_file
    