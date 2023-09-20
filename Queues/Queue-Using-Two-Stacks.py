from os import *
from sys import *
from collections import *
from math import *

class Queue:

    # Stacks to be used in the operations.
    def __init__(self):
        self.stk1 = []  # This stack is used to enqueue elements.
        self.stk2 = []  # This stack is used to dequeue elements.

    # Enqueues 'X' into the queue. Returns true after enqueuing.
    def enqueue(self, X):
        # Write your code here
        """
        Appends the element 'X' to the `stk1` stack.
        """
        self.stk1.append(X)
        return True

    """
      Dequeues top element from queue. Returns -1 if the queue is empty, 
      otherwise returns the popped element.
    """
    def dequeue(self):
        # Write your code here
        """
        If the `stk1` stack is empty, then the queue is empty.
        Otherwise, we repeatedly pop elements from the `stk1` stack and 
        append them to the `stk2` stack until only one element is left 
        in the `stk1` stack. We then pop that element from the `stk1` stack 
        and return it.
        """
# Check if the first stack (stk1) is empty, indicating an empty queue
if len(self.stk1) == 0:
    return -1  # Return -1 to indicate an empty queue

# Transfer all elements from stk1 to stk2, leaving one element in stk1
while len(self.stk1) != 1:
    ele = self.stk1.pop()
    self.stk2.append(ele)

# Pop the last element (the front element) from stk1
first = self.stk1.pop()

# Transfer all elements from stk2 back to stk1, maintaining the queue order
while len(self.stk2) != 0:
    ele = self.stk2.pop()
    self.stk1.append(ele)

# Return the dequeued (front) element
return first

