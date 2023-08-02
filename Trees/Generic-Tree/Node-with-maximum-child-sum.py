from sys import stdin, setrecursionlimit
import queue

# Set the recursion limit to handle large trees
setrecursionlimit(10**6)

# TreeNode class definition
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    # Method to calculate the sum of data for the current node and its children
    def calculate_sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

# Function to find the node with the maximum sum of its data and data of its children
def maxSumNode(tree):
    if tree is None:
        return None
    
    # Calculate the sum of data for the current node and its children
    node_sum = tree.calculate_sum()
    
    max_sum = float('-inf')
    max_node = None

    # Iterate through the children of the current node
    for child in tree.children:
        # Recursively find the node with the maximum sum among children
        max_node1 = maxSumNode(child)
        child_sum = max_node1.calculate_sum()

        # Update the maximum sum and corresponding node if needed
        if child_sum > max_sum:
            max_sum = child_sum
            max_node = max_node1
    
    # Compare the sum of the current node and its children with the maximum sum found so far
    if node_sum > max_sum:
        return tree
    
    return max_node

# Function to create a tree from the given input array using level-wise construction
def createLevelWiseTree(arr):
    root = TreeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(childCount):
            temp = TreeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main function
if __name__ == "__main__":
    # Read the input array
    arr = list(map(int, input().strip().split()))
    
    # Create the tree using the input array
    tree = createLevelWiseTree(arr)
    
    # Find the node with the maximum sum and print its data
    max_sum_node = maxSumNode(tree)
    print(max_sum_node.data)
