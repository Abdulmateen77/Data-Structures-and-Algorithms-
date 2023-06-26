class Node:
def init(self, data):
self.data = data
self.next = None

#Function to calculate the length of a linked list
#head: the head node of the linked list
def length(head):
"""
This function iterates through the linked list, counting the number of nodes,
and returns the length of the linked list.
"""
temp = head  # Start with the head node
lengthLL = 0

# Traverse the linked list until the end is reached (temp is None)
while temp is not None:
    lengthLL += 1  # Increment the length counter
    temp = temp.next  # Move to the next node

return lengthLL
