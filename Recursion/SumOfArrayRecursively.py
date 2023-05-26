def sumArray(arr, length):
    # Base case: if the length is less than or equal to 0, return 0
    if length <= 0:
        return 0
    
    # Recursive case: sum the elements from index 0 to length-1 and add it to the sum of remaining elements
    else:
        return sumArray(arr, length-1) + arr[length-1]


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)

n = int(input())  # Input the number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Input the array elements
length = len(arr)  # Calculate the length of the array
print(sumArray(arr, length))  # Print the sum of the array elements
