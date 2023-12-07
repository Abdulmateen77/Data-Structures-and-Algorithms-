#Import the sys module to use stdin for input
from sys import stdin

 #Function to find the number with the maximum frequency in an array
def maximumFreq(arr):
    # Create an empty dictionary to store number frequencies
    dict = {}
    
    # Count the frequency of each number using a dictionary
    for num in arr:
        dict[num] = dict.get(num, 0) + 1
    
    # Initialize variables to track the maximum frequency and corresponding number
    maximum = -1
    maxNum = None
    
    # Find the number with the maximum frequency
    for num in arr:
        if dict[num] > maximum:
            maximum = dict[num]
            maxNum = num
    
    # Return the number with the maximum frequency
    return maxNum

# Read the input for the array size
ArrayInput = int(input())

# Read the input array elements and convert them to integers
arr = list(int(i) for i in input().strip().split(' ')[:ArrayInput])

# Call the maximumFreq function to find the number with the maximum frequency
result = maximumFreq(arr)

# Print the result (number with maximum frequency) to the console
print(result)
