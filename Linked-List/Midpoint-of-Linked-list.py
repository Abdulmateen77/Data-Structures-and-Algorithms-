class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def midPoint(head):
    # Function to find the middle point of a linked list
    # Takes the head of the linked list as input
    
    if head is None:
        return head
    # If the head is None (empty list), return None
    
    slow = head
    fast = head
    # Initialize two pointers, slow and fast, both pointing to the head node
    
    while fast.next is not None and fast.next.next is not None:
        # Loop until the next node of fast and the next node of the next node of fast are not None
        
        slow = slow.next
        # Move the slow pointer one step ahead
        
        fast = fast.next.next
        # Move the fast pointer two steps ahead
        
    return slow
    # Return the slow pointer, which points to the middle node of the list
