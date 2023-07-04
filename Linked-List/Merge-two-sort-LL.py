class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def mergeTwoSortedLinkedLists(head1, head2):
    # Function to merge two sorted linked lists into a single sorted linked list
    # Takes the heads of the two linked lists as input
    
    if head1 is None and head2 is None:
        return None
    # If both heads are None (both lists are empty), return None
    
    if head1 is None:
        return head2
    # If head1 is None, return head2
    
    if head2 is None:
        return head1
    # If head2 is None, return head1
    
    finalHead = None
    finalTail = None
    # Initialize finalHead and finalTail as None
    
    if head1.data > head2.data:
        finalHead = head2
        finalTail = head2
        head2 = head2.next
    else:
        finalHead = head1
        finalTail = head1
        head1 = head1.next
    # Determine the initial values of finalHead and finalTail based on which head has a smaller value
    
    while head1 is not None and head2 is not None:
        # Loop until either head1 or head2 becomes None
        
        if head1.data < head2.data:
            finalTail.next = head1
            finalTail = finalTail.next
            head1 = head1.next
        else:
            finalTail.next = head2
            finalTail = finalTail.next
            head2 = head2.next
        # Compare the data of the current nodes of head1 and head2
        # Connect the smaller node to the final list using finalTail and move the corresponding head and finalTail
        
        if head1 is not None:
            finalTail.next = head1
        if head2 is not None:
            finalTail.next = head2
        # If any of the heads are not None, connect the remaining nodes to the final list
        
    return finalHead
    # Return the head of the merged sorted linked list
