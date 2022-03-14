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
    
    # Read file
    with open(input_file, 'r') as f:
        data = f.read()

    # Get frequency table from data
    frequencies = collections.Counter(data)
    
    
    


def build_tree(frequencies):
    ''' Build Huffman tree and return its root '''
    q = create_queue_from_frequencies(frequencies)
    while q.qsize() > 1:
        left = q.get()[1]
        right = q.get()[1]
    
    

def create_queue_from_frequencies(frequencies):
    ''' Create priority queue from frequency table '''