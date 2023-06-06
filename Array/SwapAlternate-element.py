def swapAlternate(arr, n):
    # Traverse the array from index 0 to len(arr)-1 with a step size of 2
    for i in range(len(arr)-1):
        # Check if the current index is even
        if i % 2 == 0:
            # Swap the current element with the next element
            arr[i], arr[i+1] = arr[i+1], arr[i]

# Main
n = int(input())  # Number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Array of integers

# Call the swapAlternate function
swapAlternate(arr, n)

# Print the modified array
for num in arr:
    print(num, end=' ')
