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
    root = build_tree(frequencies)
    
    


def build_tree(frequencies):
    ''' Build Huffman tree and return its root '''
    queue = create_queue_from_frequencies(frequencies)
    while queue.qsize() > 1:
        left = queue.get()[1]
        right = queue.get()[1]
        new_node = Node('', left.freq + right.freq, left, right)
        queue.put((new_node.freq, new_node))

    root = queue.get()[1]
    return root
    

def create_queue_from_frequencies(frequencies):
    ''' Create priority queue from frequency table '''
    queue = PriorityQueue()
    for k, v in frequencies.items():
        n = Node(k, v)
        queue.put((n.freq, n))
    return queue