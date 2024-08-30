from sys import stdin
import queue


def reverseKElements(inputQueue, k):
    #Check if k is 0 or greater than queue size, return the input queue as it is
    if k == 0 or k > inputQueue.qsize():
        return inputQueue
    
    stack = []  # Stack to temporarily store k elements from the front of the queue

    #Retrieve k elements from the front of the queue and push them onto the stack
    for i in range(k):
        stack.append(inputQueue.get())

    #Pop elements from the stack and enqueue them back into the input queue
    while len(stack) != 0:
        inputQueue.put(stack.pop())

    # Rotate the remaining elements in the input queue by k positions
    for i in range(inputQueue.qsize() - k):
        inputQueue.put(inputQueue.get())
    
    return inputQueue

'''-------------- Utility Functions --------------'''

# Takes a list as a stack and returns whether the stack is empty or not
def isEmpty(stack):
    return len(stack) == 0

# Takes a list as a stack and returns the element at the top
def top(stack):
    # Assuming the stack is never empty
    return stack[len(stack) - 1]


def takeInput():
    # Read values for n and k
    n_k = list(map(int, stdin.readline().strip().split(" ")))
    n = n_k[0]
    k = n_k[1]

    # Create a queue and enqueue values from input
    qu = queue.Queue()
    values = list(map(int, stdin.readline().strip().split()))

    for i in range(n):
        qu.put(values[i])

    return k, qu


# Main
k, qu = takeInput()

# Reverse the k elements in the queue
qu = reverseKElements(qu, k)

# Print the elements of the modified queue
while not qu.empty():
    print(qu.get(), end=" ")
