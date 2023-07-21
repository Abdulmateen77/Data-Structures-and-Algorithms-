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

def printLevelWise(root):
    # Function to print the binary tree in level-order fashion with each level on a new line

    # Base case: If the root is None, there's nothing to print
    if root is None:
        return
    
    # Create a queue to store the nodes of the current level
    q = queue.Queue()
    q.put(root)

    # Loop until the queue is empty (all levels are processed)
    while not q.empty():
        levelSize = q.qsize()  # Get the number of nodes at the current level

        # Loop through the nodes at the current level and print their data
        for ele in range(levelSize):
            current_Node = q.get()
            print(current_Node.data, end=" ")

            # Enqueue the left and right children, if they exist, for the next level
            if current_Node.left:
                q.put(current_Node.left)
        
            if current_Node.right:
                q.put(current_Node.right)
        
        print()  # Move to the next line after printing the nodes of the current level

# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    # If there's only one element in the list, it represents an empty tree, so return None
    if length == 1:
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

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

# Main function
root = takeInput()

# Print the binary tree in level-order fashion with each level on a new line
printLevelWise(root)
