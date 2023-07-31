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


# Main function to build the tree and test the printTree function
if __name__ == "__main__":
    # Create the root node
    root = TreeNode(1)

    # Create child nodes and add them to the root
    child1 = TreeNode(2)
    child2 = TreeNode(3)
    child3 = TreeNode(4)

    root.children.append(child1)
    root.children.append(child2)
    root.children.append(child3)

    # Create grandchildren nodes and add them to child1
    grandchild1 = TreeNode(5)
    grandchild2 = TreeNode(6)

    child1.children.append(grandchild1)
    child1.children.append(grandchild2)

    # Print the tree
    printTree(root)
