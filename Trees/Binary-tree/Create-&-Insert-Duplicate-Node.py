# Importing necessary modules and setting recursion limit to handle large binary trees
from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertDuplicateNode(root):
    # Function to insert a duplicate node for each node in the Binary tree

    # Base case: If the root is None, return None (empty tree)
    if root is None:
        return None

    # Create a new node with the data value same as the current root
    duplicateNode = BinaryTreeNode(root.data)

    # Link the new node to the left of the current root
    duplicateNode.left = root.left

    # Link the left child of the current root to the new node
    root.left = duplicateNode

    # Recursively insert duplicate nodes for left and right subtrees
    insertDuplicateNode(duplicateNode.left)  # Left subtree of the duplicate node
    insertDuplicateNode(root.right)    # Right subtree of the original root

    # Return the modified root
    return root

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

# Insert duplicate nodes for each node in the binary tree
insertDuplicateNode(root)

# Print the modified binary tree level-wise
printLevelWise(root)
