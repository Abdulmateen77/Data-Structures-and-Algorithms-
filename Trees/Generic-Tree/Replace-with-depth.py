from sys import stdin, setrecursionlimit
# Increase recursion limit to handle large trees
setrecursionlimit(10**6)

# Definition of TreeNode class
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# Function to replace node data with its depth in the tree
def replacewithDepth(tree, d=0):
    if tree is None:
        return None

    # Replace node data with depth value
    tree.data = d

    # Recursively replace data of children nodes with their depths
    for child in tree.children:
        replacewithDepth(child, d+1)
    
    return tree

# Function to create a level-wise tree from an array
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Function to print each level of the tree on a new line
def printLevelAtNewLine(tree):
    q = [tree]
    newq = []
    while q:
        parent = q.pop(0)
        print(parent.data, end=' ')
        for child in parent.children:
            newq.append(child)
        if len(q) == 0:
            q = newq
            newq = []
            print()  # Move to the next line for the next level

# Main code
arr = list(int(x) for x in stdin.readline().strip().split())
tree = createLevelWiseTree(arr)
replacewithDepth(tree)
printLevelAtNewLine(tree)
