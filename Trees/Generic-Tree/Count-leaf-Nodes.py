import sys

# Define the treeNode class
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
    def __str__(self):
        return str(self.data)

# Function to count the number of leaf nodes in the tree
def leafNodeCount(tree):
    # Base case: if the node has no children, it is a leaf node
    if tree.children == []:
        return 1
    leaf = 0
    
    # Count leaf nodes in each child
    for child in tree.children:
        leaf = leaf + leafNodeCount(child)
        
    return leaf

# Function to create a level-wise generic tree
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main
sys.setrecursionlimit(10**6)

# Read input and create the generic tree
arr = list(int(x) for x in input().strip().split(' '))
tree = createLevelWiseTree(arr)

# Print the count of leaf nodes
print(leafNodeCount(tree))
