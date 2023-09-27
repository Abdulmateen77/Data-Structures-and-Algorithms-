import heapq  # Import the heapq module for heap operations

def kthLargest(lst, k):
    heap = lst[0:k]  # Create a heap with the first k elements
    heapq.heapify(heap)  # Convert the list into a min-heap

    # Iterate through the remaining elements
    for num in lst[k:]:
         # If the current number is greater than the smallest element in the heap
        if num > heap[0]: 
            # Remove the smallest element from the heap
            heapq.heappop(heap)  
            # Push the current number onto the heap
            heapq.heappush(heap, num)  
    # Return the root (smallest element) of the heap, which is the kth largest element
    return heap[0] 

# Main code
# Input the total number of elements in the list
n = int(input())  
 # Input the list elements
lst = list(int(i) for i in input().strip().split(' ')) 
# Input the value of k for finding the kth largest element
k = int(input())  
# Find the kth largest element using the function
ans = kthLargest(lst, k)
#Print the kth largest element
print(ans)
