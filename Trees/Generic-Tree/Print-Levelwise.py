import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def printLevelWiseTree(root):
    # Function to print the tree in level order traversal format
    if root is None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        # Print the data of the current node
        print(current.data, end=":")

        # List to store the data of children of the current node
        children_data = []
        for i, child in enumerate(current.children):
            children_data.append(str(child.data))
            # Add the children to the queue for further processing
            q.put(child)

        # Print the data of children in comma-separated format
        print(",".join(children_data))

def createLevelWiseTree(arr):
    # Function to create a level-wise tree from the given array
    root = treeNode(int(arr[0]))
    q = [root]
    size = len(arr)
    i = 1
    while i < size:
        parent = q.pop(0)
        childCount = int(arr[i])
        i += 1
        for j in range(childCount):
            temp = treeNode(int(arr[i + j]))
            parent.children.append(temp)
            q.append(temp)
        i += childCount
    return root

# Main function
arr = list(input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
