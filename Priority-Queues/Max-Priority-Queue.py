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

    # Get the maximum priority (highest value) element in the priority queue
    def getMax(self):
        if self.isEmpty():
            return None
        return self.pq[0].priority
    
    # Move a newly inserted element up the priority queue to maintain the max heap property
    def __procolateUp(self):
        childIndex = self.getSize() - 1

        while childIndex > 0:
            parentIndex = (childIndex - 1) // 2

            if self.pq[childIndex].priority > self.pq[parentIndex].priority:
                self.pq[childIndex], self.pq[parentIndex] = self.pq[parentIndex], self.pq[childIndex]
                childIndex = parentIndex
            else:
                break
    
    # Insert an element with a given priority into the priority queue
    def insert(self, ele, priority):
        pqNode = PriorityQueueNode(ele, priority)
        self.pq.append(pqNode)  # Add the new element to the end of the list
        self.__procolateUp()    # Move the element up to maintain the max heap property
    
    # Move an element down the priority queue to maintain the max heap property
    def __procolateDown(self):
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2

        while leftChildIndex < self.getSize():
            maxIndex = parentIndex

            if self.pq[maxIndex].priority < self.pq[leftChildIndex].priority:
                maxIndex = leftChildIndex
            
            if rightChildIndex < self.getSize() and self.pq[maxIndex].priority < self.pq[rightChildIndex].priority:
                maxIndex = rightChildIndex

            if maxIndex == parentIndex:
                break

            self.pq[parentIndex], self.pq[maxIndex] = self.pq[maxIndex], self.pq[parentIndex]

            parentIndex = maxIndex

            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2 

    # Remove and return the maximum priority element from the priority queue
    def removeMax(self):
        if self.isEmpty():
            return None
        ele = self.pq[0].priority  # Store the priority of the maximum priority node
        self.pq[0] = self.pq[self.getSize() - 1]
        self.pq.pop()
        self.__procolateDown()  # Move the new root element down to maintain the max heap property
        return ele

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
        myPq.insert(element, element)  # Insert the element into the priority queue
    elif choice == 2:
        print(myPq.getMax())  # Print the maximum priority element in the priority queue
    elif choice == 3:
        print(myPq.removeMax())  # Remove and print the maximum priority element
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
