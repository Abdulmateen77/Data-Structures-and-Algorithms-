#Set the recursion limit to handle large trees
sys.setrecursionlimit(10**6)
#Import sys module to set the recursion limit
import sys
#Import stdin from sys module to read input
from sys import stdin

# Definition of the TreeNode class representing a node in a generic tree
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

# Function to calculate the height of a generic tree using recursion
def HeightofTree(root):
    # Base case: If the root is None, the height is 0
    if root is None:
        return 0

    # Initialize the height as 1 for the current node
    height = 1

    # Iterate through all the children of the current node
    for child in root.children:
        # Recursively calculate the height of each child and update the maximum height
        height = max(height, 1 + HeightofTree(child))

    # Return the calculated height for the current node
    return height

# Function to create a generic tree using level-wise input
def createLevelWiseTree(arr):
    # Extract the root data from the first element of the array
    root = treeNode(int(arr[0]))
    # Create a queue to store nodes for level-wise tree construction
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        # Get the parent node from the front of the queue
        parent = q.pop(0)
        # Get the number of children for the current parent
        childCount = int(arr[i])
        i += 1
        # Add the children nodes to the parent node and enqueue them for further processing
        for j in range(0, childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

def main():
    # Read the input as a list of integers from the user
    arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
    # Create the generic tree
    root = createLevelWiseTree(arr)

    # Calculate the height of the generic tree
    height = HeightofTree(root)

    # Print the height of the tree
    print(height)

if __name__ == "__main__":
    main()
