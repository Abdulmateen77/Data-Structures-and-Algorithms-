def checkMaxHeap(lst):
    # Get the total number of elements in the list
    n = len(lst)

    # Iterate through the list up to the second-to-last element
    for i in range(n - 1):
        leftIndex = 2 * i + 1  # Calculate the index of the left child
        rightIndex = leftIndex + 1  # Calculate the index of the right child
        
        # Check if the left child index is within the bounds of the list
        if leftIndex < n and lst[leftIndex] > lst[i]:
            return False  # If the left child is greater, it violates max-heap property
        
        # Check if the right child index is within the bounds of the list
        if rightIndex < n and lst[rightIndex] > lst[i]:
            return False  # If the right child is greater, it violates max-heap property
            
    return True  # If all conditions are met, the list is a max-heap

# Main Code
# Input the total number of elements in the list
n = int(input()) 
 # Input the list elements
lst = list(int(i) for i in input().strip().split(' ')) 
# Check if the input list is a max-heap and print the result
print('true') if checkMaxHeap(lst) else print('false')
