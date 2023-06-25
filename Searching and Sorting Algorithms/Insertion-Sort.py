def insertionSort(arr: List[int], n: int) -> None:
"""
Insertion sort builds the final sorted array one element at a time.
It iterates over the array, shifting elements to the right until it finds the correct position
to insert the current element in the sorted portion of the array.
"""
for i in range(n):
    j = i
    
    # Shift elements to the right until the correct position for the current element is found
    while j > 0 and arr[j-1] > arr[j]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        j -= 1
