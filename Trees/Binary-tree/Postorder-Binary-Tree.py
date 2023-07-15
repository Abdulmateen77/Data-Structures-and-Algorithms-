from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def postOrder(root):
    # Function to perform pre-order traversal of a binary tree
    # Your code goes here
    if root is None:
        return
    
    # Recursively traverse the left subtree
    leftRoot = postOrder(root.left)

    # Recursively traverse the right subtree
    rightRoot = postOrder(root.right)

    # Print the data of the current node
    print(root.data, end=" ")


# Taking level-order input using fast I/O method
def takeInput():
    levelOrder = list(map(int, stdin.readline().strip().split(" ")))
    start = 0

    length = len(levelOrder)

    # Create the root node of the binary tree
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


# Main
root = takeInput()

# Perform post-order traversal of the binary tree and print the nodes
postOrder(root)
