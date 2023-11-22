import sys
#set the maximum recursion depth to handle large trees
sys.setrecursionlimit(3000)

from sys import stdin

#TreeNode class to represent each node of the generic tree
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return str(self.data)

# Function to find and return the node with the maximum data in the generic tree
def maxDataNode(tree):
    if tree == None:
        return None
    
    max_node = tree

    # Iterate through each child of the current node
    for child in tree.children:

        # Recursively find the node with the maximum data in each child subtree
        max_child = maxDataNode(child)

        # Compare the maximum node of the child subtree with the current max node
        if max_child is not None and max_child.data > max_node.data:
            max_node = max_child
    
    return max_node

# Function to create a level-wise generic tree from the input array
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

# Main function to read input, create the tree, and find the node with maximum data
if __name__ == "__main__":
    arr = list(int(x) for x in stdin.readline().rstrip().rsplit())
    tree = createLevelWiseTree(arr)
    print(maxDataNode(tree).data)
