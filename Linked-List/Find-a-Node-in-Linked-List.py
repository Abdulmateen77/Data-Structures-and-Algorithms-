# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def findNode(head, n):
    # Function to find the position of a node with a given value in the linked list
    curr = head
    count = 0
    while curr is not None:
    # If the current node's data matches the given value, return the position
        if curr.data == n:
            return count
        count += 1
        curr = curr.next

    # If the node is not found, return -1
    return -1
