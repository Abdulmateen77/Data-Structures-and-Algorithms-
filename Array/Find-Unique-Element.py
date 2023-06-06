def findUnique(arr):
    # Initialize a variable to store the unique number
    unique_num = 0

    # Iterate through each element in the array
    for num in arr:
        # XOR operation between unique_num and the current element
        unique_num ^= num

    # The unique number will be stored in unique_num
    return unique_num

# Main
n = int(input())  # Number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Array of integers

# Call the findUnique function
unique = findUnique(arr)

# Print the unique number
print(unique)
