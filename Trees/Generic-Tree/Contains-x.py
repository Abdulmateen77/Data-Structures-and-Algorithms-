from sys import stdin, setrecursionlimit
import queue

#Set recursion limit to handle large trees
setrecursionlimit(10**6)

#Definition of a tree node
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

#Function to check if a tree contains a specific value x
def containsX(tree, x):
    #Base case: If tree is empty, return False
    if tree == None:
        return False
    
    # If current node's data is equal to x, return True
    if tree.data == x:
        return True
    
    # Recursively check each child node for the value x
    for child in tree.children:
        if containsX(child, x):
            return True
    
    # If x is not found in the current node or its children, return False
    return False

# Function to create a tree from the given input
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0,childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main function to read input and perform the search
def main():
    # Read input for tree elements
    arr = list(int(x) for x in stdin.readline().strip().split())
    
    # Read input for the value to search
    x = int(stdin.readline().strip())
    
    # Create the tree
    tree = createLevelWiseTree(arr)
    
    # Check if the tree contains the value x and print the result
    if containsX(tree, x):
        print('true')
    else:
        print('false')

if __name__ == "__main__":
    main()
