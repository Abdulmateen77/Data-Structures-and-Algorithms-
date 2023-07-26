import queue

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def findPathBST(root, data):
    # Function to find the path from the root to the node with the given data in the Binary search tree (BST).
    # If the data is not found in the BST, it returns None.
    # The path is represented as a list of nodes' data in the order from the root to the target node.
    
    if root is None:
        return None
    
    if root.data == data:
        return [root.data]  # Return the data as a list with a single element if the data is found in the current node.
    
    if root.data > data:
        # If the data is less than the current node's data, search in the left subtree.
        left_output = findPathBST(root.left, data)
        if left_output is not None:
            left_output.append(root.data)  # Append the current node's data to the path if the data is found in the left subtree.
            return left_output

    else:
        # If the data is greater than the current node's data, search in the right subtree.
        right_output = findPathBST(root.right, data)
        if right_output is not None:
            right_output.append(root.data)  # Append the current node's data to the path if the data is found in the right subtree.
            return right_output

def buildLevelTree(levelorder):
    # Function to build a binary tree from its level-order representation and returns the root of the tree.
    
    index = 0
    length = len(levelorder)
    if length <= 0 or levelorder[0] == -1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        current_node = q.get()
        left_child = levelorder[index]
        index += 1
        if left_child != -1:
            left_node = BinaryTreeNode(left_child)
            current_node.left = left_node
            q.put(left_node)
        right_child = levelorder[index]
        index += 1
        if right_child != -1:
            right_node = BinaryTreeNode(right_child)
            current_node.right = right_node
            q.put(right_node)
    return root

# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
data = int(input())
path = findPathBST(root, data)
if path is not None:
    for ele in path:
        print(ele, end=' ')
