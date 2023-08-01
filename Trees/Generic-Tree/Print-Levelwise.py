import queue

class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def printLevelWiseTree(root):
    if root is None:
        return

    q = queue.Queue()
    q.put(root)

    while not q.empty():
        current = q.get()
        print(current.data, end=":")
        children_data = []
        for i, child in enumerate(current.children):
            children_data.append(str(child.data))
            q.put(child)

        print(",".join(children_data))


def createLevelWiseTree(arr):
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

# Main
arr = list(input().strip().split(' '))
tree = createLevelWiseTree(arr)
printLevelWiseTree(tree)
