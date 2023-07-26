from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def countNodesGreaterThanX(root, x):
    # Function to count the number of nodes in a binary tree that are greater than x
    # Your code goes here
    if root is None:
        return 0
    
    # Recursively count the number of nodes greater than X in the left subtree
    leftCount = countNodesGreaterThanX(root.left, x)
    
    # Recursively count the number of nodes greater than X in the right subtree
    rightCount = countNodesGreaterThanX(root.right, x)

    # Check if the current node's data is greater than x
    if root.data > x:
        return 1 + leftCount + rightCount
    else:
        return leftCount + rightCount


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
x = int(stdin.readline().strip())

# Count the number of nodes in the binary tree that are greater than x
count = countNodesGreaterThanX(root, x)
print(count)
