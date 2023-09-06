import heapq, os

class BinaryTreeNode:
    def __init__(self,value,freq):
        self.value = value
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq
    
    def __eq__(self,other):
        return self.freq == other.freq

class huffmanCoding:
    def __init__(self,path):
        self.path = path
        self.__heap = []
        self.__code = {}
        self.__reverseCode = {}
    
    
