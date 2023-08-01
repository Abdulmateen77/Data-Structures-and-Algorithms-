import sys
from sys import stdin

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def HeightofTree(root):
    if root is None:
        return 0
    
    height = 1

    for child in root.children:
        height = max(height, 1 + HeightofTree(child))

    return height

def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i<size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root
  
def main():
    # Set the recursion limit to handle large trees
    sys.setrecursionlimit(10**6)

    arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
    # Create the generic tree
    root = createLevelWiseTree(arr)

    # Calculate the height of the generic tree
    height = HeightofTree(root)

    # Print the height of the tree
    print( height)

if __name__ == "__main__":
    main()
