from entity.node import Node
from queue import PriorityQueue
import collections
import os
from helpers import utility
import pickle

def compress(input_file, output_path):
    ''' Compress input_file, store it in output_path and then
    return output_file '''