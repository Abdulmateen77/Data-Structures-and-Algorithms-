from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

def nextLargest(tree, n):
    if tree == None:
        return None
    
    ans_node = None
    temp = None

    if tree.data > n:
        ans_node = tree
    
    for child in tree.children:
        temp = nextLargest(child, n)

        if temp is not None and (ans_node is None or (temp.data < ans_node.data and temp.data > n)):
            ans_node = temp
    
    return ans_node





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
# Main
arr = list(int(x) for x in stdin.readline().strip().split())
n = int(input())
tree = createLevelWiseTree(arr)
result_node = nextLargest(tree, n)
if result_node:
    print(result_node.data)
