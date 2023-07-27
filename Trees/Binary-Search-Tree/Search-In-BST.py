import queue

# Representation of a Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to search for a node with value 'k' in a Binary Search Tree (BST)
def searchInBST(root, k):
    # If root is None, the tree is empty, so the node cannot be found.
    if root is None:
        return False
    
    # If the current node's data matches the target 'k', return True as it is found.
    if root.data == k:
        return True
    
    # If the target 'k' is less than the current node's data, search in the left subtree.
    elif root.data > k:
        return searchInBST(root.left, k)
    
    # If the target 'k' is greater than the current node's data, search in the right Subtree.
    else:
        return searchInBST(root.right, k)

# Function to build a Binary Tree from its level order representation.
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

# Main function
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
k = int(input())
ans = searchInBST(root, k)
if ans:
    print("true")
else:
    print("false")
