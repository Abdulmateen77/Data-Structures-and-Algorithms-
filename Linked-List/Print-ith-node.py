class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printIthNode(head, i):
    """
    This function prints the value of the ith node in the linked list.
    If the ith node does not exist, it returns None.
    """
    count = 0
    curr = head
    
    # Traverse the linked list until the ith node is reached or the end is reached (curr is None)
    while curr and count < i:
        curr = curr.next
        count += 1
    
    # Check if the ith node exists in the linked list
    if curr:
        print(curr.data)  # Print the data of the ith node
    else:
        return None

# Example usage:
# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

printIthNode(head, 2)
# Output: 3 (Value of the 2nd node, considering 0-based indexing)
