def checkNumber(arr, x):
    # Base case: If the array is empty, return False
    size = len(arr)
    if size == 0:
        return False
    
    # If the first element of the array matches the target number, return True
    elif arr[0] == x:
        return True
    
    # Recursively check if the target number exists in the smaller array
    smallarr = checkNumber(arr[:size-1], x)
    
    # Return True if the target number was found in the smaller array or if the last element of the original array matches the target number
    return smallarr or x == arr[size-1]

# Main
from sys import setrecursionlimit
setrecursionlimit(11000)  # Increase recursion limit to handle large input

# Read input from the user
n = int(input())  # Number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Array of integers
x = int(input())  # Target number to check

# Call the checkNumber function and print the result
if checkNumber(arr, x):
    print('true')
else:
    print('false')
