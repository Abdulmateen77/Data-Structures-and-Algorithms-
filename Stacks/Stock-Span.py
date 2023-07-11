from sys import stdin

def stockSpan(price, n):
    # Create an empty stack to store indices
    stack = []
    answer = []

    for i in range(n):
        # Remove indices from stack while the price at the current index is greater than the price at the top of the stack
        while len(stack) != 0 and price[stack[-1]] < price[i]:
            stack.pop()

        if len(stack) == 0:
            # If the stack is empty, append the current index + 1 to the answer list
            answer.append(i + 1)
        else:
            # If the stack is not empty, append the difference between the current index and the top of the stack to the answer list
            answer.append(i - stack[-1])

        # Push the current index to the stack
        stack.append(i)

    return answer

# Utility function to print a list
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

    print()

def takeInput():
    size = int(stdin.readline().strip())

    if size == 0:
        return list(), 0

    price = list(map(int, stdin.readline().strip().split(" ")))

    return price, size


# Main
price, n = takeInput()

output = stockSpan(price, n)
printList(output)
