# Function to find the number with maximum frequency in an array
def maximumFreq(arr):
    dict = {}
    
    # Count the frequency of each number using a dictionary
    for num in arr:
        dict[num] = dict.get(num, 0) + 1
    
    maximum = -1
    maxNum = None
    
    # Find the number with the maximum frequency
    for num in arr:
        if dict[num] > maximum:
            maximum = dict[num]
            maxNum = num
    
    return maxNum

# Read the input for the array size
ArrayInput = int(input())

# Read the input array elements
arr = list(int(i) for i in input().strip().split(' ')[:ArrayInput])

# Call the maximumFreq function and print the result
print(maximumFreq(arr))
