def bubbleSort(arr: List[int], n: int) -> None:
"""
Bubble sort repeatedly swaps adjacent elements if they are in the wrong order,
until the entire array is sorted in ascending order.
"""
i = n - 1

# Iterate over the array from the last element to the second element
while i > 1:
    j = 0
    
    # Compare adjacent elements and swap if necessary
    while j <= i - 1:
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
        
        j += 1
    
    i -= 1
