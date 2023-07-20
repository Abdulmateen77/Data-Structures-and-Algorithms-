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

### This Solution gives us the Time Complexity of O(N^2)###
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



"""
    Time Complexity : O(N)
    Space Complexity : O(N)
	
    Where 'N' is the number of nodes in the given binary tree.
"""

def getDiameter(root, height):

    if (root == None):
    
        # Height and diameter of an empty tree will be 0.
        height[0] = 0
        return 0
    

    # To store the height of left and right subtrees.
    leftHeight = [0]
    rightHeight = [0]

    # Recur for left subtree and get the height as well as diameter.
    leftDiameter = getDiameter(root.left, leftHeight)

    # Recur for right subtree and get the height as well as diameter.
    rightDiameter = getDiameter(root.right, rightHeight)

    # Update the height of the given binary tree.
    height[0] = max(leftHeight[0], rightHeight[0]) + 1

    # Diameter of given binary tree.
    diameter = max(leftDiameter, max(rightDiameter, leftHeight[0] + rightHeight[0]))

    return diameter


def diameterOfBinaryTree(root):

    # Initialize a variable to store the height of the of binary tree.
    height = [0]

    # Recursive function to find diameter.
    return 1 + getDiameter(root, height)
