class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        self.numNodes = 0
    
    def printTreeHelper(self, root, data):
        # Helper function to print the tree in the required format using pre-order traversal.
        if root == None:
            return
        
        print("{}:".format(root.data), end="")

        if root.left != None:
            print("L:{}".format(root.left.data), end=",")
        
        if root.right != None:
            print("R:{}".format(root.right.data), end="")

        print()
        self.printTreeHelper(root.left, data)
        self.printTreeHelper(root.right, data)

    def printTree(self):
        # Function to print the binary search tree (BST) in the required format.
        # It calls the helper function to perform pre-order traversal and print the tree nodes.
        self.printTreeHelper(self.root, data)
    
    def searchHelper(self, root, data):
        # Helper function to search for a given data in the binary search tree (BST).
        # If the data is found, it returns the data; otherwise, it returns None.
        if root == None:
            return None
        
        if root.data == data:
            return root.data
        
        if root.data > data:
            return self.searchHelper(root.left, data)
        else:
            return self.searchHelper(root.right, data)

    def search(self, data):
        # Function to search for a given data in the binary search tree (BST).
        # It calls the helper function to perform the search.
        return self.searchHelper(self.root, data)

    def insertHelper(self, root, data):
        # Helper function to insert a new node with the given data in the binary search tree (BST).
        # If the node is already present, it returns the root node.
        if root == None:
            Node = BinaryTreeNode(data)
            return Node
        
        if root.data >= data:
            root.left = self.insertHelper(root.left, data)
            return root
        else:
            root.right = self.insertHelper(root.right, data)
            return root
        
    def insert(self, data):
        # Function to insert a new node with the given data in the binary search tree (BST).
        # It calls the helper function to perform the insertion.
        self.numNodes += 1
        self.root = self.insertHelper(self.root, data)        

    def min(self, root):
        # Helper function to find the minimum value node in the binary search tree (BST).
        if root == None:
            return 10000
        
        if root.left == None:
            return root.data
        
        return self.min(root.left)
    
    def deleteHelper(self, root, data):
        # Helper function to delete the node with the given data from the binary search tree (BST).
        # It returns a boolean value indicating whether the deletion is successful or not, and the new root node after deletion.
        if root == None:
            return False, None
        
        if root.data > data:
            deleted, newLeftNode = self.deleteHelper(root.left, data)
            root.left = newLeftNode
            return deleted, root
        
        if root.data < data:
            deleted, newRightNode = self.deleteHelper(root.right, data)
            root.right = newRightNode
            return deleted, root
        
        # Root is leaf
        if root.left == None and root.right == None:
            return True, None
        
        # Root has one child
        if root.left == None:  
            return True, root.right

        if root.right == None:
            return True, root.left
        
        # Root has children
        replacement = self.min(root.right)
        root.data = replacement

        deleted, newRightNode = self.deleteHelper(root.right, replacement)
        root.right = newRightNode

        return True, root

    def delete(self, data):
        # Function to delete the node with the given data from the binary search tree (BST).
        # It calls the helper function to perform the deletion.
        deleted, newRoot = self.deleteHelper(self.root, data)

        if deleted:
            self.numNodes -= 1
        
        self.root = newRoot
        return deleted
    
    def count(self):
        #Function to get the total number of nodes in the binary search tree (BST).
        return self.numNodes
        
b = BST()
q = int(input())
while q > 0:
    li = [int(ele) for ele in input().strip().split()]
    choice = li[0]
    q -= 1
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
