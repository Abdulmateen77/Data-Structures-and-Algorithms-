from sys import stdin

# This class defines the node structure for a singly linked list.
class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

# This class defines the queue data structure. It has methods for enqueueing, dequeuing, getting the front element, getting the size, and checking if the queue is empty.
class Queue:

    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__count = 0
        self.__front = 0

    # Returns the size of the queue.
    def getSize(self):
        return self.__count

    # Checks if the queue is empty.
    def isEmpty(self):
        return self.getSize() == 0

    # Adds a new element to the queue.
    def enqueue(self, data):
        newNode = Node(data)
        if self.__head == None:
            self.__head = newNode
            self.__tail = newNode
        else:
            self.__tail.next = newNode
            self.__tail = newNode

        self.__count += 1

    # Removes the first element from the queue.
    def dequeue(self):
        if self.__count == 0:
            return -1

        removedEle = self.__head.data
        self.__head = self.__head.next

        self.__count -= 1

        return removedEle

    # Returns the first element in the queue.
    def front(self):
        if self.__count == 0:
            return -1

        return self.__head.data

# This is the main function of the program. It takes input from the user and performs the corresponding operations on the queue.
def main():
    q = int(stdin.readline().strip())

    queue = Queue()

    while q > 0:
        inputs = stdin.readline().strip().split(" ")
        choice = int(inputs[0])

        if choice == 1:
            data = int(inputs[1])
            queue.enqueue(data)

        elif choice == 2:
            print(queue.dequeue())

        elif choice == 3:
            print(queue.front())

        elif choice == 4:
            print(queue.getSize())

        else:
            if queue.isEmpty():
                print("true")
            else:
                print("false")

        q -= 1

if __name__ == "__main__":
    main()
