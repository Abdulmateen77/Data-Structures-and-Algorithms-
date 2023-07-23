from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def rootToLeafPathsSumToK(root, k, path, path_sum):
    # Your code goes here
    if root is None:
        return
    
    path.append(root.data)
    path_sum += root.data

    if root.left is None and root.right is None:
        if path_sum == k:
            print(" ".join(map(str, path)))

    rootToLeafPathsSumToK(root.left, k, path, path_sum)
    rootToLeafPathsSumToK(root.right, k, path, path_sum)

    # Remove the current node from the path and update the path sum (backtrack)
    path.pop()
    path_sum -= root.data

def printPaths(root, K):
    # Function to print all root-to-leaf paths with sum K
    path = []  # To store the current path
    path_sum = 0  # To store the sum of nodes in the current path
    rootToLeafPathsSumToK(root, K, path, path_sum)

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

    while not q.empty():
        currentNode = q.get()

        leftChild = levelOrder[start]
        start += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        rightChild = levelOrder[start]
        start += 1

        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)

    return root

def printLevelWise(root):
    if root is None:
        return

    inputQ = queue.Queue()
    outputQ = queue.Queue()
    inputQ.put(root)

    while not inputQ.empty():
        while not inputQ.empty():
            curr = inputQ.get()
            print(curr.data, end=' ')
            if curr.left is not None:
                outputQ.put(curr.left)
            if curr.right is not None:
                outputQ.put(curr.right)

        print()
        inputQ, outputQ = outputQ, inputQ

# Main
root = takeInput()
k = int(stdin.readline().strip())
printPaths(root, k)
