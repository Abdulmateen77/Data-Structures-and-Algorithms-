from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def buildTree(postOrder, inOrder, n):
    # Function to build a binary tree using post-order and in-order traversals

    # Base case: If post-order list is empty, return None (empty tree)
    if len(postOrder) == 0:
        return None

    # The last element in post-order is the root data
    rootdata = postOrder[-1]

    # Create the root node using the root data
    root = BinaryTreeNode(rootdata)

    # Find the index of the root data in the in-order list to determine left and right subtrees
    rootIndexInorder = -1
    for ele in range(0, len(inOrder)):
        if inOrder[ele] == rootdata:
            rootIndexInorder = ele
            break

    # If the root data is not found in the in-order list, return None (invalid input)
    if rootIndexInorder == -1:
        return None

    # Divide the in-order list into left and right subtrees based on the rootIndexInorder index
    leftInOrder = inOrder[0:rootIndexInorder]
    rightInOrder = inOrder[rootIndexInorder + 1:]

    # Calculate the lengths of the left and right subtrees
    lengthLeft = len(leftInOrder)

    # Divide the post-order list into left and right subtrees using the lengths of the in-order subtrees
    leftPostOrder = postOrder[0:lengthLeft]
    rightPostOrder = postOrder[lengthLeft:-1]

    # Recursively build the left and right subtrees
    leftChild = buildTree(leftPostOrder, leftInOrder, n)
    rightChild = buildTree(rightPostOrder, rightInOrder, n)

    # Link the left and right subtrees to the current root node
    root.left = leftChild
    root.right = rightChild

    # Return the root node of the binary tree
    return root


'''-------------------------- Utility Functions --------------------------'''

def printLevelWise(root):
    # Function to print the binary tree level-wise using BFS traversal

    if root is None:
        return

    pendingNodes = queue.Queue()
    pendingNodes.put(root)
    pendingNodes.put(None)

    while not pendingNodes.empty():
        frontNode = pendingNodes.get()

        if frontNode is None:
            print()

            if not pendingNodes.empty():
                pendingNodes.put(None)
        else:
            print(frontNode.data, end=" ")

            if frontNode.left is not None:
                pendingNodes.put(frontNode.left)

            if frontNode.right is not None:
                pendingNodes.put(frontNode.right)


# Taking level-order input using fast I/O method
def takeInput():
    n = int(stdin.readline().strip())

    if n == 0:
        return list(), list(), 0

    postOrder = list(map(int, stdin.readline().strip().split(" ")))
    inOrder = list(map(int, stdin.readline().strip().split(" ")))

    return postOrder, inOrder, n

# Main function
postOrder, inOrder, n = takeInput()
root = buildTree(postOrder, inOrder, n)
printLevelWise(root)
