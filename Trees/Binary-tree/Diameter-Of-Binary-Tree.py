# Importing necessary modules and setting recursion limit to handle large binary trees
from sys import stdin, setrecursionlimit
import queue
setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to calculate the height of a binary tree starting from the given root
def height(root):
    if root == None:
        return 0

    # Calculate the height recursively as 1 plus the maximum of the heights of the left and right subtrees
    return 1 + max(height(root.left), height(root.right))


# Function to find the diameter of a binary tree
def diameterOfBinaryTree(root):
    # Base case: If the root is None, the diameter of the tree is 0
    if root == None:
        return 0
    
    # Calculate the height of the left and right subtrees
    lh = height(root.left)
    rh = height(root.right)

    # Calculate the maximum diameter that passes through the current root
    h = lh + rh

    # Recursively find the diameters of the left and right subtrees
    leftroot = diameterOfBinaryTree(root.left)
    rightroot = diameterOfBinaryTree(root.right)

    # Return the maximum of the following three values:
    # 1. The maximum diameter that goes through the current root (h).
    # 2. The diameter of the left subtree (leftroot).
    # 3. The diameter of the right subtree (rightroot).
    # Adding 1 to the maximum value to account for the current root node in the diameter calculation.
    return 1 + max(h, leftroot, rightroot)
