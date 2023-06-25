def binarySearch(arr: List[int], n: int, x: int) -> int:
# Function to perform binary search on a sorted array
# arr: input array
# n: length of the array
# x: element to be searched

start = 0
end = n - 1

while start <= end:
    mid = start + (end - start) // 2  # Calculate the middle index
    
    if arr[mid] == x:
        return mid  # Element found at the middle index
    
    if arr[mid] < x:
        start = mid + 1  # Search in the right half of the array
    else:
        end = mid - 1  # Search in the left half of the array

return -1  # Element not found
