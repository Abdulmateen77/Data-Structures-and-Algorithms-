class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root):
    def height(node):
        if not node:
            return 0
        return 1 + max(height(node.left), height(node.right))

    def diameter_helper(node):
        if not node:
            return 0

        # Get the height of the left and right subtrees
        lh = height(node.left)
        rh = height(node.right)

        # Calculate the diameter passing through the current node
        current_diameter = lh + rh

        # Recursively find the diameter in the left and right subtrees
        left_diameter = diameter_helper(node.left)
        right_diameter = diameter_helper(node.right)

        # Return the maximum of the current diameter and the diameters of the left and right subtrees
        return max(current_diameter, left_diameter, right_diameter)

    return diameter_helper(root)

# Example usage:
# Build the binary tree manually
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# Calculate and print the diameter of the binary tree
diameter = diameterOfBinaryTree(root)
print("Diameter of the binary tree:", diameter)
