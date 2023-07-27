class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class BST:
    
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self,root,data):
        if root == None:
            return
        
        print("{}:".format(root.data), end="")

        if root.left != None:
            print("L:{}".format(root.left.data), end=",")
        
        if root.right != None:
            print("R:{}".format(root.right.data), end="")

        print()
        self.printTreeHelper(root.left,data)
        self.printTreeHelper(root.right,data)

    def printTree(self):
        self.printTreeHelper(self.root, data)
    
    def searchHelper(self,root,data):
        if root == None:
            return None
        
        if root.data == data:
            return root.data
        
        if root.data > data:
            return self.searchHelper(root.left, data)
        
        else:
            return self.searchHelper(root.right,data)

    def search(self, data):
        return self.searchHelper(self.root,data)

    def insertHelper(self, root,data):
        if root == None:
            Node = BinaryTreeNode(data)
            return Node
        
        if root.data >= data:
            root.left = self.insertHelper(root.left,data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
        
    def insert(self, data):
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)        

    def min(self,root):
        if root == None:
            return 10000
        
        if root.left == None:
            return root.data
        
        return self.min(root.left)
    
      
    def deleteHelper(self,root,data):
        if root == None:
            return False, None
        
        if root.data > data:
            deleted, newLeftNone = self.deleteHelper(root.left, data)
            root.left = newLeftNone
            return deleted, root
        
        if root.data < data:
            deleted, newRightNone = self.deleteHelper(root.right, data)
            root.right = newRightNone
            return deleted, root
        
        #Root is leaf
        if root.left == None and root.right == None:
            return True, None
        
        #Root has one child
        if root.left == None:  
            return True, root.right

        if root.right == None:
            return True, root.left
        
        #root has children
        replacement = self.min(root.right)
        root.data = replacement

        deleted, newRightNone = self.deleteHelper(root.right,replacement)
        root.right = newRightNone

        return True, root

    def delete(self, data):
        deleted, newRoot = self.deleteHelper(self.root, data)

        if deleted:
            self.numNodes -= 1
        
        self.root = newRoot
        return deleted
        
    
    def count(self):
        return self.numNodes
        
b = BST()
q = int(input())
while (q > 0) :
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q-=1
    if choice == 1:
        data = li[1]
        b.insert(data)
    elif choice == 2:
        data = li[1]
        b.delete(data)
    elif choice == 3:
        data = li[1]
        ans = b.search(data)
        if ans is not None:
            print('true')
        else:
            print('false')
    else:
        b.printTree()
