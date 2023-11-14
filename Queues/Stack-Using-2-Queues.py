from sys import stdin
import queue

class Stack:

    #Define data members and __init__()
    def __init__(self):
        # Initialize two queues, q1 and q2
        self.q1 = queue.Queue()
        self.q2 = queue.Queue()

    '''----------------- Public Functions of Stack -----------------'''

    def getSize(self):
        # Implement the getSize() function
        # Returns the number of elements in the stack
        return self.q1.qsize()

    def isEmpty(self):
        # Implement the isEmpty() function
        # Returns True if the stack is empty, False otherwise
        return self.getSize() == 0

    def push(self, data):
        # Implement the push(element) function
        # Add the element to the stack
        self.q1.put(data)

    def pop(self):
        # Implement the pop() function
        # Removes the top element from the stack and returns it
        if self.q1.empty():
            # The stack is empty, return -1
            return -1

        # While there are more than 1 elements in the queue,
        # move all elements from q1 to q2
        while self.q1.qsize() > 1:
            ele = self.q1.get()
            self.q2.put(ele)

        # Get the element at the front of q1
        deletedEle = self.q1.get()

        # Swap the queues
        self.q1, self.q2 = self.q2, self.q1

        return deletedEle

    def top(self):
        # Implement the top() function
        # Returns the top element of the stack without removing it
        if self.q1.empty():
            # The stack is empty, return -1
            return -1

        # While there are more than 1 elements in the queue,
        # move all elements from q1 to q2
        while self.q1.qsize() > 1:
            ele = self.q1.get()
            self.q2.put(ele)

        # Get the element at the front of q1
        top = self.q1.get()

        # Put the element back in q1
        self.q2.put(top)

        # Swap the queues
        self.q1, self.q2 = self.q2, self.q1

        return top

# main
q = int(stdin.readline().strip())

stack = Stack()

while q > 0:

    inputs = stdin.readline().strip().split(" ")
    choice = int(inputs[0])

    if choice == 1:
        data = int(inputs[1])
        stack.push(data)

    elif choice == 2:
        print(stack.pop())

    elif choice == 3:
        print(stack.top())

    elif choice == 4:
        print(stack.getSize())

    else:
        if stack.isEmpty():
            print("true")
        else:
            print("false")

    q -= 1
