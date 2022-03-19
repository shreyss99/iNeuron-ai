class Node(object):

    ''' This class represents node structure in the binary tree '''
    
    def __init__(self, char, freq, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
        
        
    def is_leaf(self):
        return self.left is None and self.right is None


    def __lt__(self, temp):
        ''' Sorting criteria for inserting into priority queue '''
        
        return (self.freq < temp.freq)
        
    
    def __eq__(self, temp):
        if not isinstance(self, temp.__class__):
            return False
            
        return self.char == temp.char and self.freq == temp.freq


    def __ne__(self, temp):
        return not self.__eq__(temp)


    def __str__(self):
        return '({} : {})'.format(self.char, self.freq)