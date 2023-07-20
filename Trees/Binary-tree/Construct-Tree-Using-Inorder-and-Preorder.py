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

def buildTree(preOrder, inOrder, n):
    # Function to build a binary tree using pre-order and in-order traversals

    # Base case: If pre-order list is empty, return None (empty tree)
    if len(preOrder) == 0:
        return None
    
    # The first element in pre-order is the root data
    rootdata = preOrder[0]

    # Create the root node using the root data
    root = BinaryTreeNode(rootdata)

    # Find the index of the root data in the in-order list to determine left and right subtrees
    rootInOrder = -1
    for ele in range(0, len(inOrder)):
        if inOrder[ele] == rootdata:
            rootInOrder = ele
            break
    
    # If the root data is not found in the in-order list, return None (invalid input)
    if rootInOrder == -1:
        return None
    
    # Divide the in-order list into left and right subtrees based on the rootInOrder index
    inOrderLeft = inOrder[0:rootInOrder]
    inOrderRight = inOrder[rootInOrder + 1:]
    
    # Calculate the lengths of the left and right subtrees
    lengthLeft = len(inOrderLeft)

    # Divide the pre-order list into left and right subtrees using the lengths of the in-order subtrees
    preOrderleft = preOrder[1:lengthLeft + 1]
    preOrderRight = preOrder[lengthLeft + 1:]

    # Recursively build the left and right subtrees
    leftChild = buildTree(preOrderleft, inOrderLeft, n)
    rightChild = buildTree(preOrderRight, inOrderRight, n)

    # Link the left and right subtrees to the current root node
    root.left = leftChild
    root.right = rightChild

    # Return the root node of the binary tree
    return root


'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    # Function to print the binary tree level-wise using BFS traversal

    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()
            
            if not pendingNodes.empty():
                pendingNodes.put(None)
        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    preOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return preOrder, inOrder, n

# Main function
preOrder, inOrder, n = takeInput()
root = buildTree(preOrder, inOrder, n)
printLevelWise(root)
