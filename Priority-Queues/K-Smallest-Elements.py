# Import the heapq module, which provides heap-related functions
import heapq

# Define a function 'kSmallest' to find the k smallest elements from a list
def kSmallest(lst, k):
    # Create a heap of the first k elements
    heap = lst[0:k]
    
    # Convert the heap into a max heap using the _heapify_max function
    heapq._heapify_max(heap)
    
    # Get the total number of elements in the list
    n = len(lst)
    
    # Iterate over the remaining elements in the list
    for i in range(k, n - 1):
        # If the current element is smaller than the largest element in the heap
        if heap[0] > lst[i]:
            # Replace the largest element in the heap with the current element
            heapq._heapreplace_max(heap, lst[i])
    
    return heap  # Return the k smallest elements as a heap

# Main program starts here
# Get the total number of elements 'n' as input
n = int(input())

# Get the list of elements as input and convert them to integers
lst = list(int(i) for i in input().strip().split(' '))

# Get the value of 'k' as input
k = int(input())

# Call the kSmallest function to find the k smallest elements and store the result
ans = kSmallest(lst, k)

# Sort the resulting heap in ascending order
ans.sort()

# Print the sorted k smallest elements with space-separated values
print(*ans, sep=' ')
