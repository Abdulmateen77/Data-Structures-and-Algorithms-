def selectionSort(arr: List[int], n: int) -> None:
# Function to perform selection sort on an array
# arr: input array
# n: length of the array

for i in range(0, n - 1):
    mini = i
    
    # Find the index of the minimum element in the unsorted part of the array
    for j in range(i + 1, n):
        if arr[j] < arr[mini]:
            mini = j
    
    # Swap the minimum element with the first element of the unsorted part
    arr[mini], arr[i] = arr[i], arr[mini]
