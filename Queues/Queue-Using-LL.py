from sys import stdin

#This class defines the node structure for a singly linked list.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

#This class defines the queue data structure. It has methods for enqueueing, dequeuing, getting the front element, getting the size, and checking if the queue is empty.
class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
        self.__front = 0

    #Returns the size of the queue.
    def getSize(self):
        return self.__count

    #Checks if the queue is empty.
    def isEmpty(self):
        return self.getSize() == 0

    #Adds a new element to the queue.
    def enqueue(self, data):
        newNode = Node(data)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode

        self.__count += 1

#Dequeue method: Removes and returns the front element from the queue.
def dequeue(self):
    # Check if the queue is empty (count is 0)
    if self.__count == 0:
        return -1  # Return -1 to indicate an empty queue
    
    # Store the data of the current front element to be removed
    removedEle = self.__head.data

    # Move the head pointer to the next element in the queue
    self.__head = self.__head.next

    # Decrease the count of elements in the queue
    self.__count -= 1

    # Return the removed element
    return removedEle

# Front method: Returns the data of the first element in the queue without removing it.
def front(self):
    # Check if the queue is empty (count is 0)
    if self.__count == 0:
        return -1  # Return -1 to indicate an empty queue

        return self.__head.data

# This is the main function of the program. It takes input from the user and performs the corresponding operations on the queue.
def main():
    # Read the number of queries (q) from standard input
    q = int(stdin.readline().strip())

    # Create an empty queue using a custom Queue class (not shown in this code snippet)
    queue = Queue()

    # Loop through the queries
    while q > 0:
        # Read and split the input line into a list of strings
        inputs = stdin.readline().strip().split(" ")
        
        # Convert the first element of the input list to an integer (choice)
        choice = int(inputs[0])

        # Perform operations based on the choice value
        if choice == 1:
            # Enqueue (add) an integer data element to the queue
            data = int(inputs[1])
            queue.enqueue(data)

        elif choice == 2:
            # Dequeue (remove) and print the front element of the queue
            print(queue.dequeue())

        elif choice == 3:
            # Print the front element of the queue without removing it
            print(queue.front())

        elif choice == 4:
            # Print the size (number of elements) of the queue
            print(queue.getSize())

        else:
            # Check if the queue is empty and print the result (true/false)
            if queue.isEmpty():
                print("true")
            else:
                print("false")

        # Decrement the query counter
        q -= 1

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the main function to start executing the program
    main()

