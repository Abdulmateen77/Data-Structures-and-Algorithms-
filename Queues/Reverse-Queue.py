from sys import stdin, setrecursionlimit
import queue

setrecursionlimit(10 ** 6)

def reverseQueue(inputQueue):
    # Check if the size of the input queue is less than or equal to 1, no need to reverse
    if inputQueue.qsize() <= 1:
        return inputQueue
    
    # Get the front element of the queue
    lastElement = inputQueue.get()

    # Reverse the remaining elements of the queue using recursion
    reverseQueue(inputQueue)

    # Put the front element at the end of the reversed queue
    inputQueue.put(lastElement)



'''-------------- Utility Functions --------------'''

def takeInput():
    # Read the number of elements in the queue
    n = int(stdin.readline().strip())

    # Create a queue and populate it with the given values
    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])

    return qu

# Main
t = int(stdin.readline().strip())

while t > 0:
    qu = takeInput()
    reverseQueue(qu)
    
    # Print the reversed queue
    while not qu.empty():
        print(qu.get(), end=" ")
        
    print()
    
    t -= 1
