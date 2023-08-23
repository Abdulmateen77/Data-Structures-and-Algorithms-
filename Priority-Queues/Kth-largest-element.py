import heapq  # Import the heapq module for heap operations

def kthLargest(lst, k):
    heap = lst[0:k]  # Create a heap with the first k elements
    heapq.heapify(heap)  # Convert the list into a min-heap

    # Iterate through the remaining elements
    for num in lst[k:]:
        if num > heap[0]:  # If the current number is greater than the smallest element in the heap
            heapq.heappop(heap)  # Remove the smallest element from the heap
            heapq.heappush(heap, num)  # Push the current number onto the heap
    
    return heap[0]  # Return the root (smallest element) of the heap, which is the kth largest element

# Main code
n = int(input())  # Input the total number of elements in the list
lst = list(int(i) for i in input().strip().split(' '))  # Input the list elements
k = int(input())  # Input the value of k for finding the kth largest element
ans = kthLargest(lst, k)  # Find the kth largest element using the function
print(ans)  # Print the kth largest element
