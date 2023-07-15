from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def changeToDepthTree(root, d=0):
    # Function to convert a binary tree to a depth tree
    # Your code goes here
    if root is None:
        return
    
    # Recursively convert the left subtree to a depth tree
    leftRoot = changeToDepthTree(root.left, d+1)
    
    # Recursively convert the right subtree to a depth tree
    rightRoot = changeToDepthTree(root.right, d+1)

    # Assign the depth level as the new value for the current node
    root.data = d

    return root


def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0
    
    length = len(levelOrder)

    if length == 1:
        return None
    
    root = BinaryTreeNode(levelOrder[start])
    start += 1

    q = queue.Queue()
    q.put(root)

    # Construct the binary tree using level-order traversal
    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        # Create the left child node and link it to the current node
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        # Create the right child node and link it to the current node
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root


def inOrder(root):
    # Function to perform in-order traversal of the tree
    if root is None:
        return 

    # Recursively traverse the left subtree
    inOrder(root.left)
    
    # Print the data of the current node
    print(root.data, end=" ")
    
    # Recursively traverse the right subtree
    inOrder(root.right)


# Main
root = takeInput()

# Convert the binary tree to a depth tree
changeToDepthTree(root)

# Print the in-order traversal of the depth tree
inOrder(root)
