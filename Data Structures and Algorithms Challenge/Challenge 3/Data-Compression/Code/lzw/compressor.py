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
    
    
    
    def encode(data):
    
    # Initialize dictionary
    dic = {chr(c): c for c in range(0, 256)}
    chars = dic.keys()
    max_code = 255