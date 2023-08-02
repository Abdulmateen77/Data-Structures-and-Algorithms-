from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
import queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def calculate_sum(self):
        ans = self.data
        for child in self.children:
            ans += child.data
        return ans

def maxSumNode(tree):
    if tree is None:
        return None
    
    node_sum = tree.calculate_sum()
    
    max_sum = float('-inf')
    max_node = None

    for child in tree.children:
        max_node1 = maxSumNode(child)
        child_sum = max_node1.calculate_sum()

        if child_sum > max_sum:
            max_sum = child_sum
            max_node = max_node1
    
    if node_sum > max_sum:
        return tree
    
    return max_node

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

# Main
arr = list(map(int, input().strip().split()))
tree = createLevelWiseTree(arr)
max_sum_node = maxSumNode(tree)
print(max_sum_node.data)
