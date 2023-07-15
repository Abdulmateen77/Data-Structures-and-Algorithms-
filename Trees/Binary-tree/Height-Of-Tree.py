from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    # Function to calculate the height of a binary tree
    # Your code goes here
    if root is None:
        return 0
    
    # Recursively calculate the height of the left subtree
    leftCount = height(root.left)
    
    # Recursively calculate the height of the right subtree
    rightCount = height(root.right)

    # Return the maximum of left subtree height and right subtree height, plus 1 for the current node
    return 1 + max(leftCount, rightCount)


# Taking level-order input using fast I/O method
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


# Main
root = takeInput()

# Calculate the height of the binary tree
h = height(root)
print(h)
