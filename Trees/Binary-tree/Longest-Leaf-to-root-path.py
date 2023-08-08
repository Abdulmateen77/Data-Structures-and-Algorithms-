import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find the longest path from leaf to root in a binary tree
def longestPath(root):
    if root is None:
        return []

    # Recursively find the longest path in the left and right subtrees
    left_path = longestPath(root.left)
    right_path = longestPath(root.right)

    # Compare the lengths of left and right paths and return the longer one
    if len(left_path) > len(right_path):
        return left_path + [root.data]
    else:
        return right_path + [root.data]

# Function to build a level-order tree
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right = rightNode
            q.put(rightNode)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

# Find and print the longest path from leaf to root
path = longestPath(root)
for ele in path:
    print(ele)
