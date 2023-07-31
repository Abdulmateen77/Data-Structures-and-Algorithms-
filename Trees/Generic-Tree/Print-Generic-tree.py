
def printTree(root):
  #Edge case not a base case
  if root == None:
    return

print(root.data, ":", end=" ")

for child in root.children:
  print(child.root, ",", end =" ")

print()

for child in root.children:
  printTree(child)
