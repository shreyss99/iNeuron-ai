from entity.node import Node
from queue import PriorityQueue
import collections
import os
from helpers import utility
import pickle

def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then
    return output_file '''
    
    # Get input file name and extension
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    # Store output file name and path
    output_filename = input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)