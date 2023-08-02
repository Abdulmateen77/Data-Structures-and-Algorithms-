from sys import stdin, setrecursionlimit
# Increase recursion limit to handle large trees
setrecursionlimit(10**6)

# Definition of TreeNode class
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

# Function to find the next largest node in the tree
def nextLargest(tree, n):
    if tree is None:
        return None
    
    ans_node = None
    temp = None

    # If current node's data is greater than n, it can potentially be the next largest
    if tree.data > n:
        ans_node = tree
    
    # Explore the children nodes
    for child in tree.children:
        temp = nextLargest(child, n)

        # If temp is not None and satisfies the conditions, update ans_node
        if temp is not None and (ans_node is None or (temp.data < ans_node.data and temp.data > n)):
            ans_node = temp
    
    return ans_node

# Function to create a level-wise tree from an array
def createLevelWiseTree(arr):
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(0, childCount):
            temp = treeNode(int(arr[i+j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

