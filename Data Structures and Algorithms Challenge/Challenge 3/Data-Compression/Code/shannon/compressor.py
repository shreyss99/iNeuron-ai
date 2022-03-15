from entity.node import Node
from operator import attrgetter
from helpers import utility
import os
import collections
import pickle

def compress(input_file, output_path):

    '''Get input file details and output file details'''
    input_filename, input_fileext = os.path.splitext(os.path.basename(input_file))
    
    output_filename = 'Compressed_' + input_filename + '.txt'
    output_file = os.path.join(output_path, output_filename)
    
    # Open file
    with open(input_file, 'r') as f:
        data = f.read()

    # Calculate frequencies of elements using counter collection
    frequencies = collections.Counter(data)
    
    nodes = create_nodes_from_frequencies(frequencies)
    root = build_tree(nodes)
    
    
    
    def build_tree(nodes):
    ''' Build binary tree from node list '''
    
    
    
    def create_nodes_from_frequencies(frequencies):
    ''' Create node list from frequency table and sort it '''