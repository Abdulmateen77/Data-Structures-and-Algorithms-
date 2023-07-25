import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def isNodePresent(root, x):
    # Function to check if a given node with value x exists in the tree.
    # Returns True if found, false otherwise.
    
    if root == None:
        return False

    if root.data == x:
        return True

    # Recursively check if the node with value x exists in the left or right subtree.
    return isNodePresent(root.left, x) or isNodePresent(root.right, x)


# To build the tree
def buildLevelTree(levelorder):
    # Function to build a binary tree from the given level order traversal.
    # Returns the root of the constructed binary tree.

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

        # Process left child
        leftChild = levelorder[index]
        index += 1

        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left = leftNode
            q.put(leftNode)

        # Process right child
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

x = int(input())

present = isNodePresent(root, x)

if present:
    print('true')
else:
    print('false')
