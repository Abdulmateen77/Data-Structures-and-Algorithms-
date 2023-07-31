import sys
import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = list()

def inputLevelWise(li):
    # Initialize the index to traverse the input list 'li'.
    i = 0

    # Get the data of the root node.
    data = li[i]
    i += 1

    # If the data is -1, it represents an empty node, so return None.
    if data == -1:
        return None

    # Create the root node with the given data.
    root = TreeNode(data)

    # Create a queue to keep track of nodes at each level.
    q = queue.Queue()
    q.put(root)

    # Continue until all nodes in the queue are processed.
    while not q.empty():
        # Get the front node from the queue.
        frontNode = q.get()

        # Get the number of children for the front node.
        noOfChildren = li[i]
        i += 1

        # Get the list of children data for the front node.
        childrenArray = li[i: i + noOfChildren]

        # Create child nodes for each child data and add them to the front node.
        for childData in childrenArray:
            childNode = TreeNode(childData)
            frontNode.children.append(childNode)
            q.put(childNode)

        # Move the index to the next position after processing all children.
        i = i + noOfChildren

    return root

def sumOfAllNodes(root):
    # Base case: If the root is None, return 0 as there are no nodes.
    if root is None:
        return 0
    
    # Start the sum with the data of the current root node.
    sum = root.data

    # Calculate the sum recursively for each child node and add it to the total sum.
    for child in root.children:
        sum = sum + sumOfAllNodes(child)

    return sum

# Main function to create the tree and calculate the sum of all nodes.
if __name__ == "__main__":
    # Set the recursion limit to handle large trees.
    sys.setrecursionlimit(10**6)

    # Read the input list of integers.
    li = [int(elem) for elem in list(input().strip().split())]

    # Construct the tree from the input list.
    root = inputLevelWise(li)

    # Calculate the sum of all nodes in the tree and print the result.
    print(sumOfAllNodes(root))
