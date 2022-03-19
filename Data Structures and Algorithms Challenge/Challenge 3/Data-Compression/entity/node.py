class Node(object):

    ''' This class represents node structure in the binary tree '''
    
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right