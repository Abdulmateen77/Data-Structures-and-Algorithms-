from sys import stdin

# Function to sort an array containing only 0s and 1s
def sortZeroesAndOne(arr, n):
    s = 0  # Start pointer
    e = n - 1  # End pointer
    
    # Iterate through the array using the two pointers approach
    while s <= e:
        if arr[s] == 0:
            s += 1  # Increment start pointer if the element is 0
        else:
            arr[s], arr[e] = arr[e], arr[s]  # Swap the elements at start and end pointer if the element is 1
            e -= 1  # Decrement end pointer

# Taking Input Using Fast I/O
def takeInput():
    n = int(stdin.readline().strip())  # Read the number of elements in the array
    if n == 0:
        return list(), 0  # Return an empty list and 0 if the array is empty
    arr = list(map(int, stdin.readline().strip().split(" ")))  # Read the elements of the array
    return arr, n

# Function to print the elements of an array
def printList(arr, n):
    for i in range(n):
        print(arr[i], end=' ')  # Print each element separated by a space
    print()  # Print a newline character to separate output

# Main
t = int(stdin.readline().strip())  # Read the number of test cases

# Iterate through each test case
while t > 0:
    arr, n = takeInput()  # Read the input array and its size
    sortZeroesAndOne(arr, n)  # Sort the array containing only 0s and 1s
    printList(arr, n)  # Print the sorted array
    print()  # Print an empty line to separate test cases
    t -= 1  # Decrement the number of test cases
