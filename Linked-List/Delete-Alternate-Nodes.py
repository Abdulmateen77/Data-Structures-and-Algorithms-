# Following is the node structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def deleteAlternateNodes(head):
    # Function to delete alternate nodes in a linked list
    # Write your code here
    
    # If the head is None or only one node exists, no deletion is required
    if head is None or head.next is None:
        return head
    
    prev = head  # Variable to track the previous node
    now = head.next  # Variable to track the current node
  
    # Traverse the linked list and delete alternate nodes
    while prev is not None and now is not None: 
          
        # Change the next link of the previous node to skip the current node
        prev.next = now.next
  
        # Free the memory occupied by the current node
        now = None
  
        # Update the prev and now pointers to the next pair of nodes
        prev = prev.next
        if prev is not None:
            now = prev.next

    return head
