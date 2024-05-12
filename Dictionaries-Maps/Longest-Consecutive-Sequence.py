from sys import stdin

def longestConsecutiveSubsequence(arr, n): 
    #Function to find the longest consecutive subsequence within the array.
    #It takes the array 'arr' of length 'n' as input.
    #Create a set to efficiently check for presence of elements.
    Numset = set(arr)
    
    # Initialize variables to store the starting and ending elements of the longest sequence.
    ans_start = 0
    ans_end = 0
    
    # Initialize variable to keep track of the maximum length of consecutive subsequence.
    max_length = 0
    
    # Iterate through each element in the array.
    for element in arr:
        # Check if the previous consecutive element (element - 1) is not present in the set.
        if element - 1 not in Numset:
            # Initialize a variable to keep track of the current element being considered.
            curr_ele = element
            
            # Find the length of the consecutive subsequence starting from the current element.
            while curr_ele in Numset:
                curr_ele += 1
            
            # Update the maximum length and the starting and ending elements of the sequence.
            if curr_ele - element > max_length:
                max_length = curr_ele - element
                ans_start = element
                ans_end = curr_ele - 1
    
    # Return the starting and ending elements of the longest consecutive subsequence as a list.
    return [ans_start, ans_end]

def takeInput():
    # Function to take input using fast I/O from stdin.
    n = int(stdin.readline().strip())
    if n == 0:
        return list(), 0
    arr = list(map(int, stdin.readline().strip().split()))
    return arr, n

# Main function to read input, find the longest consecutive subsequence, and print the result.
arr, n = takeInput()
ans = longestConsecutiveSubsequence(arr, n)
# Print the starting and ending elements of the longest sequence.
print(*ans)
