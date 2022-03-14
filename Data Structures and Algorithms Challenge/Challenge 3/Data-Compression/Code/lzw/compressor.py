import os

def compress(input_file, output_path):
	'''Get input file name and extension'''
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    output_filename = input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)