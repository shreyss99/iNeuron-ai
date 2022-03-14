import os

def compress(input_file, output_path):
	'''Get input file name and extension'''
    
    # Get input file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)
    
    with open(input_file, 'r') as f:
        data = f.read()

    codes = encode(data)