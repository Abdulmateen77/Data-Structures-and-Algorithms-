from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

def reverseStack(inputStack, extraStack):
    # Base case: if the stack has 0 or 1 element, it's already reversed
    if len(inputStack) <= 1:
        return

    # Move all elements except the last one to the extra stack
    while len(inputStack) != 1:
        ele = inputStack.pop()
        extraStack.append(ele)

    # Remove the last element from the input stack
    lastElement = inputStack.pop()

    # Move the elements back from the extra stack to the input stack
    while len(extraStack) != 0:
        ele = extraStack.pop()
        inputStack.append(ele)

    # Recursive call to reverse the remaining elements in the input stack
    reverseStack(inputStack, extraStack)

    # Add the last element back to the input stack
    inputStack.append(lastElement)

'''-------------- Utility Functions --------------'''

# Checks whether a stack is empty
def isEmpty(stack):
    return len(stack) == 0

# Takes input for the stack
def takeInput():
    size = int(stdin.readline().strip())
    inputStack = []

    if size == 0:
        return inputStack

    values = list(map(int, stdin.readline().strip().split(" ")))
    inputStack = values
    return inputStack

# Main function
inputStack = takeInput()
emptyStack = []

reverseStack(inputStack, emptyStack)

# Print the reversed stack
while not isEmpty(inputStack):
    print(inputStack.pop(), end=" ")
