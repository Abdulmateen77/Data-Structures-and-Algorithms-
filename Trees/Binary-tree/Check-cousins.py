import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to get the level of a node in the tree
def getLevelwiseNode(root, node, level = 0):
    # Base case: If the root is None, return 0
    if root == None:
        return 0
    
    # If the data of the current root matches the node we are looking for, return the current level
    if root.data == node:
        return level
    
    # Recursively search for the node in the left subtree
    leftlevel = getLevelwiseNode(root.left, node, level + 1)
    if leftlevel != 0:
        return leftlevel

    # Recursively search for the node in the right subtree
    rightlevel = getLevelwiseNode(root.right, node, level + 1)

    # Return the level where the node is found
    return rightlevel

# Function to check if two nodes are siblings
def Issiblings(root, a, b):
    if root == None:
        return False

    # Check if both left and right children are present
    if (root.left != None and root.right != None): 
        # If the left child is 'a' and the right child is 'b', or vice versa, they are siblings
        if (root.left.data == a and root.right.data == b) or (root.left.data == b and root.right.data == a):
            return True
    
    # Recursively search for siblings in the left subtree
    if Issiblings(root.left, a, b):
        return True
    
    # Recursively search for siblings in the right subtree
    if Issiblings(root.right, a, b):
        return True

    # If no siblings found, return False
    return False

# Function to check if two nodes are cousins
def checkCousins(root, p, q):
    if root == None or p == None or q == None:
        return False
    
    # Check if nodes 'p' and 'q' are not the same, have the same level, and are not siblings
    if (p != q and getLevelwiseNode(root, p, 1) == getLevelwiseNode(root, q, 1) and Issiblings(root, p, q) == False):
        return True

    # If not cousins, return False
    else:
        return False

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
p = int(input())
q = int(input())
ans = checkCousins(root, p, q)
if ans is True:
    print('true')
else:
    print('false')
