## Read input as specified in the question.
## Print output as specified in the question.
import queue
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def getLevelwiseNode(root, node, level = 0):
    if root == None:
        return 0
    
    if root.data == node:
        return level
    
    leftlevel = getLevelwiseNode(root.left, node, level+1)
    if leftlevel != 0:
        return leftlevel

    rightlevel = getLevelwiseNode(root.right, node, level+1)

    return rightlevel


def Issiblings(root, a, b):
    if root == None:
        return False

    if(root.left != None and root.right != None): 
        if(root.left.data == a and root.right.data == b):
            return True
        if(root.left.data == b and root.right.data == a):
            return True
    
    if(Issiblings(root.left, a,b)):
        return True
    if(Issiblings(root.right, a,b)):
        return True

    return False

def checkCousins(root,p,q):
    if root == None or p == None or q == None:
        return False
    
    if(p != q and getLevelwiseNode(root, p, 1) == getLevelwiseNode(root, q, 1) and Issiblings(root, p,q)==False):
        return True

    else:
        return False 


def buildLevelTree(levelorder):
    index = 0
    length = len(levelorder)
    if length<=0 or levelorder[0]==-1:
        return None
    root = BinaryTreeNode(levelorder[index])
    index += 1
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        if leftChild != -1:
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
        rightChild = levelorder[index]
        index += 1
        if rightChild != -1:
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
    return root
# Main
levelOrder = [int(i) for i in input().strip().split()]
root = buildLevelTree(levelOrder)
p = int(input())
q = int(input())
ans = checkCousins(root,p,q)
if ans is True:
    print('true')
else:
    print('false')
