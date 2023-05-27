def partitionArray(input: [int], start: int, end: int) -> int:
    # Select the pivot element (here, it's the first element)
    pivot = input[start]
    count = 0
    
    # Count the number of elements smaller than the pivot
    for i in range(start, end + 1):
        if input[i] < pivot:
            count += 1
    
    # Move the pivot to its correct sorted position
    input[start], input[start + count] = input[start + count], input[start]
    
    pivot_index = start + count
    i = start
    j = end
    
    # Partition the array around the pivot
    while i < j:
        if input[i] < pivot:
            i += 1
        elif input[j] >= pivot:
            j -= 1
        else:
            input[i], input[j] = input[j], input[i]
            i += 1
            j -= 1
    
    return pivot_index


def quickSort(input: [int], start: int, end: int):
    # Base case: if the subarray has size 0 or 1, it is already sorted
    if start >= end:
        return
    
    # Partition the array and get the pivot index
    pivot_index = partitionArray(input, start, end)
    
    # Recursively sort the subarray to the left of the pivot
    quickSort(input, start, pivot_index - 1)
    
    # Recursively sort the subarray to the right of the pivot
    quickSort(input, pivot_index + 1, end)

input = [5, 2, 8, 1, 3]
size = len(input)
quickSort(input, 0, size - 1)
print(input)  # Output: [1, 2, 3, 5, 8]
