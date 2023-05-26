def firstIndex(arr, x, index=0):
    # Base case: if the index reaches the end of the array, return -1
    if index == len(arr):
        return -1
    # Check if the current element is equal to x
    elif arr[index] == x:
        # If found, return the current index
        return index
    else:
        # Recursive case: search for x in the remaining part of the array
        return firstIndex(arr, x, index + 1)


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n = int(input())  # Input the number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Input the array elements
x = int(input())  # Input the value to search for
print(firstIndex(arr, x, index=0))  # Print the index of the first occurrence of x
