from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following the structure used for Binary Tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getSum(root):
    # Function to calculate the sum of all nodes in a binary tree
    # Your code goes here
    if root == None:
        return 0

    # Recursively calculate the sum of nodes in the left subtree
    leftCount = getSum(root.left)

    # Recursively calculate the sum of nodes in the right subtree
    rightCount = getSum(root.right)

    # Return the sum of current node, left subtree sum, and right subtree sum
    return root.data + leftCount + rightCount


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

# Print the sum of all nodes in the binary tree
print(getSum(root))
