# Define a class to represent a node in the priority queue with an element and a priority
class PriorityQueueNode:
    def __init__(self, ele, priority):
        self.ele = ele
        self.priority = priority

# Define a class for a Priority Queue
class PriorityQueue:
    def __init__(self):
        self.pq = []  # Initialize an empty list to store priority queue elements

    # Check if the priority queue is empty
    def isEmpty(self):
        return self.getSize() == 0
    
    # Get the size of the priority queue
    def getSize(self):
        return len(self.pq)

    # Get the minimum element (highest priority) in the priority queue
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].ele
    
    # Move a newly inserted element up the priority queue to maintain the heap property
    def __percolateUp(self):
        childIndex = self.getSize() - 1
        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2
            
            if self.pq[parentIndex].priority > self.pq[childIndex].priority:
                self.pq[parentIndex], self.pq[childIndex] = self.pq[childIndex], self.pq[parentIndex]
                childIndex = parentIndex
            else:
                break
    
    # Insert an element with a given priority into the priority queue
    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)  # Add the new element to the end of the list
        self.__percolateUp()    # Move the element up to maintain the heap property

    # Move an element down the priority queue to maintain the heap property
    def __percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        while leftChildIndex < self.getSize():
            minIndex = parentIndex

            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex

            if rightChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightChildIndex].priority:
                minIndex = rightChildIndex
            
            if minIndex == parentIndex:
                break

            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2
        
    # Remove and return the minimum element (highest priority) from the priority queue
    def removeMin(self):
        if self.isEmpty():
            return None
        ele = self.pq[0].ele
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()  # Remove the last element
        self.__percolateDown()  # Move the new root element down to maintain the heap property

# Create an instance of the PriorityQueue class
myPq = PriorityQueue()

# Read user input and perform priority queue operations based on the input
curr_input = [int(ele) for ele in input().split()]
choice = curr_input[0]
i = 1
while choice != -1:
    if choice == 1:
        element = curr_input[i]
        i += 1
        # Insert the element into the priority queue
        myPq.insert(element, element)  
    elif choice == 2:
        print(myPq.getMin())  # Print the minimum element in the priority queue
    elif choice == 3:
        print(myPq.removeMin())  # Remove and print the minimum element
    elif choice == 4:
        print(myPq.getSize())  # Print the size of the priority queue
    elif choice == 5:
        if myPq.isEmpty():
            print('true')  # Print "true" if the priority queue is empty
        else:
            print('false')  # Print "false" if the priority queue is not empty
        break  # Exit the loop
    else:
        pass  # Do nothing for invalid choices
    choice = curr_input[i]
    i += 1
