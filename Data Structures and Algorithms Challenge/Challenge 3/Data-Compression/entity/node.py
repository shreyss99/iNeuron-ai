class Node(object):

    ''' This class represents node structure in the binary tree '''
    
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
        
    def is_leaf(self):
        return self.left is None and self.right is None


    def __lt__(self, other):
        ''' Sorting criteria for inserting into priority queue '''
        
        return (self.freq < other.freq)