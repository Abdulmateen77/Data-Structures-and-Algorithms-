# Define a function 'down_Heapify' to perform heapify operation on the given array at index 'i'
def down_Heapify(arr, i, n):
    parentIndex = i
    leftChildIndex = 2 * parentIndex + 1
    rightChildIndex = 2 * parentIndex + 2

    # Iterate while the left child index is within the range of the array
    while leftChildIndex < n:
        minIndex = parentIndex

        # Compare the current element with its left child
        if arr[minIndex] > arr[leftChildIndex]:
            minIndex = leftChildIndex
        
        # Check if the right child exists and compare it with the current minimum
        if rightChildIndex < n and arr[minIndex] > arr[rightChildIndex]:
            minIndex = rightChildIndex
        
        # If the minimum index remains the same as the parent index, the heap property is satisfied
        if minIndex == parentIndex:
            break
        
        # Swap the elements to maintain the heap property
        arr[minIndex], arr[parentIndex] = arr[parentIndex], arr[minIndex]

        # Update parent and child indices for the next iteration
        parentIndex = minIndex
        leftChildIndex = 2 * parentIndex + 1
        rightChildIndex = 2 * parentIndex + 2


# Define a function 'heapSort' to sort the given array using heap sort algorithm
def heapSort(arr):
    n = len(arr)

    # Build the initial heap by applying down-heapify on non-leaf nodes
    for i in range(n//2 - 1, -1, -1):
        down_Heapify(arr, i, n)

    # Perform the heap sort operation
    for i in range(n - 1, 0, -1):
        # Swap the maximum element (at the root) with the last element of the array
        arr[0], arr[i] = arr[i], arr[0]
        # Re-heapify the reduced heap
        down_Heapify(arr, 0, i)

    return


# Get the size of the array 'n' as input
n = int(input())

# Get the array elements as input and convert them to integers
arr = [int(ele) for ele in input().split()]

# Apply heap sort to the array
heapSort(arr)

# Print the sorted array
for ele in arr:
    print(ele, end=' ')
