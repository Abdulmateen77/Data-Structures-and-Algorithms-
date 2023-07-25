# Define the TreeNode class to represent nodes in the binary search tree
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Recursive function to construct a balanced binary search tree from a sorted input array
def tree(input, s ,e ):
    # Base case: If the start index (s) is greater than the end index (e), return None
    if s > e:
        return None
    
    # Calculate the middle index (mid) to find the root element of the current subtree
    mid = (s + e) // 2
    root = TreeNode(input[mid])  # Create a new node with the middle element as the root

    # Recursively construct the left subtree with elements to the left of the mid index
    root.left = tree(input, s, mid - 1)

    # Recursively construct the right subtree with elements to the right of the mid index
    root.right = tree(input, mid + 1, e)

    return root  # Return the root of the current subtree

# Function to construct a balanced binary search tree from a sorted input list (lst) of size n
def constructBST(lst, n):
    return tree(lst, 0, n - 1)  # Call the tree function with start index 0 and end index n-1

# Function to perform pre-order traversal and print the tree nodes in pre-order
def preOrder(root):
    if root is None:
        return
    print(root.data, end=' ')  # Print the current node data
    preOrder(root.left)  # Recursively traverse the left subtree
    preOrder(root.right)  # Recursively traverse the right subtree

# Main program
n = int(input())  # Read the input size n

if n > 0:
    lst = [int(i) for i in input().strip().split()]  # Read the space-separated input list
else:
    lst = []  # If n <= 0, set the input list as empty

length = len(lst)  # Get the length of the input list
root = constructBST(lst, length)  # Construct the balanced binary search tree
preOrder(root)  # Print the pre-order traversal of the tree nodes
