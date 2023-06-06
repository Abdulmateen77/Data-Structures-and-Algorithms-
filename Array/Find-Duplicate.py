def duplicateNumber(arr, n):
    # Iterate through each element in the array
    for i in range(n):
        j = 0
        # Iterate through each element again to compare with the current element
        while j < n:
            # Check if the current element indices are different and have the same value
            if i != j and arr[i] == arr[j]:
                # Return the duplicate number
                return arr[i]
            j += 1

# Main
n = int(input())  # Number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Array of integers

# Call the duplicateNumber function
duplicate = duplicateNumber(arr, n)

# Print the duplicate number
print(duplicate)
