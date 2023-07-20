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
    # Function to print the binary tree level-wise using BFS

    # Create a queue for BFS traversal
    q = queue.Queue()

    # Put the root node in the queue to start traversal
    q.put(root)

    # Perform BFS traversal until the queue is empty
    while not q.empty():
        # Get the current node from the front of the queue
        current_node = q.get()

        # Get the data of the left child if it exists, otherwise set as -1
        left_data = current_node.left.data if current_node.left else -1

        # Get the data of the right child if it exists, otherwise set as -1
        right_data = current_node.right.data if current_node.right else -1

        # Print the data of the current node along with its left and right child data
        print("{}:L:{},R:{}".format(current_node.data, left_data, right_data))

        # If the current node has a left child, add it to the queue for further traversal
        if current_node.left is not None:
            q.put(current_node.left)

        # If the current node has a right child, add it to the queue for further traversal
        if current_node.right is not None:
            q.put(current_node.right)

def takeInput():
    # Function to take level-order input and construct the binary tree

    # Read the level-order input from stdin and convert it to a list of integers
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

# Main function
root = takeInput()
printLevelWise(root)
