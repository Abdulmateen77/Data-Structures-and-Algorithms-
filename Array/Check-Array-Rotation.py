# Function to check for rotation in an array
def arrayRotateCheck(arr, n):
    # Iterate through the array elements up to the second-to-last element
    for i in range(0, n - 1):
        # Check if the current element is greater than the next element
        if arr[i] > arr[i + 1]:
            # If true, it indicates a rotation, return the index of the next element
            return i + 1
    
    # If no rotation is found, return 0 (no rotation)
    return 0
