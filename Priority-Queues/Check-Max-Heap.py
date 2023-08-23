def checkMaxHeap(lst):
    # Get the total number of elements in the list
    n = len(lst)

    # Iterate through the list up to the second-to-last element
    for i in range(n - 1):
        LeftIndex = 2*i + 1
        rightIndex = leftIndex + 1
        # Check if the current element is greater than the next element
        if leftIndex < n and  lst[leftIndex] > lst[i]:
            return False

        if rightIndex < n and lst[rightIndex] > lst[i]:
            return False
            
    return True  # If all conditions are met, the list is a max-heap

# Main Code
n = int(input())  # Input the total number of elements in the list
lst = list(int(i) for i in input().strip().split(' '))  # Input the list elements
# Check if the input list is a max-heap and print the result
print('true') if checkMaxHeap(lst) else print('false')
