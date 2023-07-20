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

# Representation of the Pair Class
class Pair:
    def __init__(self, minimum, maximum):
        self.minimum = minimum
        self.maximum = maximum

def getMinAndMax(root):
    # Function to get the minimum and maximum values in the binary tree

    # Base case: If the root is None, return a Pair object with minimum and maximum as None
    if root is None:
        return Pair(None, None)

    # Recursively get the minimum and maximum values from left and right subtrees
    left_pair = getMinAndMax(root.left)
    right_pair = getMinAndMax(root.right)

    # Initialize minimum and maximum values with the data of the current root
    minimum = root.data
    maximum = root.data

    # Update minimum and maximum based on the minimum and maximum values obtained from left and right subtrees
    if left_pair.minimum is not None and left_pair.minimum < minimum:
        minimum = left_pair.minimum

    if left_pair.maximum is not None and left_pair.maximum > maximum:
        maximum = left_pair.maximum

    if right_pair.minimum is not None and right_pair.minimum < minimum:
        minimum = right_pair.minimum

    if right_pair.maximum is not None and right_pair.maximum > maximum:
        maximum = right_pair.maximum

    # Return the Pair object containing the updated minimum and maximum values
    return Pair(minimum, maximum)

# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    # If there's only one element in the list, it represents an empty tree, so return None
    if length == 1:
        return None

    # Create the root node of the binary tree using the first element of the level-order list
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    # Create a queue to help in constructing the binary tree using BFS
    q = queue.Queue()
    q.put(root)

    # Perform BFS to construct the binary tree level by level
    while not q.empty():
        currentNode = q.get()

        # Get the left child data from the level-order list
        leftChild = levelOrder[start]
        start += 1

        # If the left child is not -1 (indicating a NULL node), create a new node and link it to the left of the current node
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        # Get the right child data from the level-order list
        rightChild = levelOrder[start]
        start += 1

        # If the right child is not -1 (indicating a NULL node), create a new node and link it to the right of the current node
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    # Return the root node of the constructed binary tree
    return root

def printLevelWise(root):
    # Function to print the binary tree level-wise using BFS traversal

    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left != None:
                outputQ.put(curr.left)
            if curr.right != None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ

# Main function
root = takeInput()

# Get the minimum and maximum values from the binary tree
pair = getMinAndMax(root)

# Print the minimum and maximum values
print(str(pair.minimum) + " " + str(pair.maximum))
