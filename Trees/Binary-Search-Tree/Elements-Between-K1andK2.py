# Import the queue module to use Queue data structure for level-order traversal
import queue

# Definition of the BinaryTreeNode class representing a node in the binary tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to print all nodes in the binary search tree (BST) that fall within the range [k1, k2]
def elementsInRangeK1K2(root, k1, k2):
    if root is None:
        return
    
    # Perform an in-order traversal of the BST
    # If the current node's value is greater than or equal to k1, explore the left subtree
    if root.data >= k1:
        elementsInRangeK1K2(root.left, k1, k2)

    # If the current node's value is between k1 and k2 (inclusive), print the node's data
    if k1 <= root.data <= k2:
        print(root.data, end=" ")

    # If the current node's value is less than or equal to k2, explore the right subtree
    if root.data <= k2:
        elementsInRangeK1K2(root.right, k1, k2)

# Function to build a binary tree from the given level-order traversal list
def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    
    # Create the root node
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)

    # Build the binary tree using level-order traversal
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
# Take the level-order traversal input for the binary tree and build the tree
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)

# Take the range [k1, k2] as input and print all nodes in the BST within this range
k1, k2 = (int(i) for i in input().strip().split())
elementsInRangeK1K2(root, k1, k2)
