class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def printTree(root):
    # Base case: If the root is None (empty tree), return.
    if root is None:
        return

    # Print the data of the current root node.
    print(root.data, ":", end=" ")

    # Print the data of each child node separated by commas.
    for child in root.children:
        print(child.data, ",", end=" ")

    # Move to the next line to separate the output of each node.
    print()

    # Recursively call the printTree function for each child node.
    for child in root.children:
        printTree(child)
