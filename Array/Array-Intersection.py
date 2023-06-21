def intersection(arr1, arr2, n, m):
# Function to find the intersection of two sorted arrays
# arr1: first sorted array
# arr2: second sorted array
# n: length of arr1
# m: length of arr2

arr1.sort()  # Sort arr1 in ascending order
arr2.sort()  # Sort arr2 in ascending order

i = 0  # Pointer for arr1
j = 0  # Pointer for arr2

while i < n and j < m:
    if arr1[i] < arr2[j]:
        # If current element in arr1 is smaller, move the pointer i
        i += 1
    elif arr2[j] < arr1[i]:
        # If current element in arr2 is smaller, move the pointer j
        j += 1
    else:
        # If both elements are equal, print the element and move both pointers
        print(arr1[i], end=" ")
        i += 1
        j += 1 
