from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

# Following is the structure used to represent the Binary Tree Node
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def nodesAtDistanceK(root, target, k):
    # Helper function to perform DFS and print nodes at distance K from the target node
    def dfs(node, dist):
        if node is None:
            return
        
        if dist == k:
            print(node.data)  # Print the node data if the distance matches K
            return
        
        dfs(node.left, dist + 1)  # Move to the left child with an increased distance
        dfs(node.right, dist + 1)  # Move to the right child with an increased distance

    # Helper function to find the target node and return its distance from the root
    def findTarget(node):
        if node is None:
            return -1
            
        if node.data == target:
            dfs(node, 0)  # If the target node is found, start DFS from this node
            return 1
        
        left_dist = findTarget(node.left)  # Check the left subtree for the target node
        right_dist = findTarget(node.right)  # Check the right subtree for the target node

        if left_dist > 0:
            if left_dist == k:
                print(node.data)  # Print the node data if the left child is at distance K
            dfs(node.right, left_dist + 1)  # Move to the right child with an increased distance
            return left_dist + 1
        
        if right_dist > 0:
            if right_dist == k:
                print(node.data)  # Print the node data if the right child is at distance K
            dfs(node.left, right_dist + 1)  # Move to the left child with an increased distance
            return right_dist + 1
        
        return -1

    findTarget(root)  # Call the function to find the target node and print nodes at distance K

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
            print(curr.data, end=' ')  # Print the data of the current node
            if curr.left is not None:
                outputQ.put(curr.left)  # Add the left child to the output queue
            if curr.right is not None:
                outputQ.put(curr.right)  # Add the right child to the output queue

        print()  # Move to the next line after printing the current level
        inputQ, outputQ = outputQ, inputQ  # Swap the queues for the next level

# Main
root = takeInput()  # Take input for the binary tree
target_k = stdin.readline().strip().split(" ")  # Read the target node and distance K

target = int(target_k[0])  # Extract the target node value
k = int(target_k[1])  # Extract the distance K

nodesAtDistanceK(root, target, k)  # Print nodes at distance K from the target node
