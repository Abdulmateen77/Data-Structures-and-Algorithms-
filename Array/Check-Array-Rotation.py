#Function to check for rotation in an array
def arrayRotateCheck(arr, n):
    # Iterate through the array elements up to the second-to-last element
    for i in range(0, n - 1):
        # Check if the current element is greater than the next element
        if arr[i] > arr[i + 1]:
            # If true, it indicates a rotation, return the index of the next element
            return i + 1
    
    #If no rotation is found, return 0 (no rotation)
    return 0

#Test case 1: Array with no rotation
arr1 = [1, 2, 3, 4, 5]
n1 = len(arr1)
print(arrayRotateCheck(arr1, n1))  # Expected output: 0 (No rotation)

#Test case 2: Array with rotation at the beginning
arr2 = [4, 5, 1, 2, 3]
n2 = len(arr2)
print(arrayRotateCheck(arr2, n2))  # Expected output: 2 (Rotation at index 2)

#Test case 3: Array with rotation in the middle
arr3 = [3, 4, 5, 1, 2]
n3 = len(arr3)
print(arrayRotateCheck(arr3, n3))  # Expected output: 3 (Rotation at index 3)

#Test case 4: Array with rotation at the end
arr4 = [2, 3, 4, 5, 1]
n4 = len(arr4)
print(arrayRotateCheck(arr4, n4))  # Expected output: 4 (Rotation at index 4)

#Test case 5: Array with a single element
arr5 = [42]
n5 = len(arr5)
print(arrayRotateCheck(arr5, n5))  # Expected output: 0 (No rotation)
