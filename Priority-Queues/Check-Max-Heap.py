def checkMaxHeap(lst):
    # Get the total number of elements in the list
    n = len(lst)

    # Iterate through the list up to the second-to-last element
    for i in range(n - 1):
        # Check if the current element is greater than the next element
        if lst[i] > lst[i + 1]:
            continue  # If condition is met, continue to the next iteration
        
        else:
            return False  # If condition is not met, the list is not a max-heap
    
    return True  # If all conditions are met, the list is a max-heap

# Main Code
n = int(input())  # Input the total number of elements in the list
lst = list(int(i) for i in input().strip().split(' '))  # Input the list elements
# Check if the input list is a max-heap and print the result
print('true') if checkMaxHeap(lst) else print('false')
