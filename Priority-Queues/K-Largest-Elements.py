import heapq  # Importing the heapq module for min-heap operations

def kLargest(lst, k):
    heap = lst[0:k]  # Create a heap of the first k elements from the list
    heapq.heapify(heap)  # Convert the list into a min-heap
    n = len(lst)  # Total number of elements in the list
    
    # Iterate over the remaining elements in the list
    for i in range(k, n):
        if heap[0] < lst[i]:  # If the smallest element in the heap is smaller than the current element
            heapq.heapreplace(heap, lst[i])  # Replace the smallest element with the current element
    return heap  # Return the k largest elements in a min-heap

# Main Code
n = int(input())  # Input the total number of elements in the list
lst = list(int(i) for i in input().strip().split(' '))  # Input the list elements
k = int(input())  # Input the value of k for finding k largest elements
ans = kLargest(lst, k)  # Call the kLargest function to get the k largest elements
print(*ans, sep='\n')  # Print the k largest elements separated by newlines
