#Importing required modules
from sys import stdin  # Importing the stdin module to take input
import sys  # Importing the sys module
import heapq as heap  # Importing the heapq module and aliasing it as 'heap'

#Class to define a node for a linked list
class LinkedListNode:
    def __init__(self, data):
        self.data = data  # Initialize the node's data
        self.next = None  # Initialize the next pointer to None
        
#Class to implement a Queue using linked list
class Queue:
    def __init__(self):
        self.head = None  # Initialize the head of the queue to None
        self.tail = None  # Initialize the tail of the queue to None
        self.size = 0  # Initialize the size of the queue to 0
        
    # Enqueue a new element to the queue
    def enqueue(self, data):
        newNode = LinkedListNode(data)  # Create a new linked list node with the given data
        if self.head is None:
            self.head = self.tail = newNode  # If the queue is empty, set both head and tail to the new node
        else:
            self.tail.next = newNode  # Set the next pointer of the current tail to the new node
            self.tail = newNode  # Update the tail to the new node
        self.size += 1  # Increase the size of the queue by 1
        return
        
    #Dequeue an element from the queue
    def dequeue(self):
        if self.head is None:
            return None  # If the queue is empty, return None
        data = self.head.data  # Get the data of the head node
        self.head = self.head.next  # Update the head to the next node
        self.size -= 1  # Decrease the size of the queue by 1
        return data
    
    #Get the size of the queue
    def getSize(self):
        return self.size  # Return the size of the queue

    # Check if the queue is empty
    def isEmpty(self):
        if self.head is None:
            return True  # Return True if the head is None, indicating an empty queue
        return False
    
    # Peek at the front element of the queue
    def peek(self):
        if self.head is None:
            return None  # Return None if the head is None
        return self.head.data  # Return the data of the head node
    
# Function to simulate buying tickets with given priorities
def buyTicket(arr, n, k):
    priorityQueue = []  # Initialize an empty list to represent the priority queue
    
    # Push negated elements to the priority queue to create a max heap
    for i in range(n):
        heap.heappush(priorityQueue, -arr[i])  # Push the negation of the element to create a max heap

    q = Queue()  # Initialize an instance of the Queue class

    for i in range(n):
        q.enqueue(arr[i])  # Enqueue the original priorities into the queue
    
    time = 0  # Initialize the time counter

    # Simulate the process of buying tickets
    while not q.isEmpty():
        if q.peek() == -priorityQueue[0]:
            time += 1
            q.dequeue()  # Dequeue the element from the queue
            heap.heappop(priorityQueue)  # Pop the element from the priority queue
            if k == 0:
                return time
            else:
                k -= 1
        else:
            q.enqueue(q.dequeue())
            if k == 0:
                k = q.getSize() - 1
            else:
                k -= 1
    
    return time  # Return the total time taken to buy all tickets

# Taking input using fast I/O
def takeInput():
    n = int(stdin.readline().strip())  # Input the number of elements
    if n == 0:
        return n, list(), int(stdin.readline().strip())  # Return 0 and empty list if n is 0
    arr = list(map(int, stdin.readline().strip().split(" ")))  # Input the priorities as a list
    k = int(stdin.readline().strip())  # Input the value of k
    return n, arr, k

# Main function
sys.setrecursionlimit(10**6)  # Set the recursion limit
n, arr, k = takeInput()  # Input n, arr, and k
print(buyTicket(arr, n, k))  # Call the buyTicket function and print the result
