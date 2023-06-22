#brute force approach
def duplicateNumber(arr, n):
    # Iterate through each element in the array
    for i in range(n):
        j = 0
        # Iterate through each element again to compare with the current element
        while j < n:
            # Check if the current element indices are different and have the same value
            if i != j and arr[i] == arr[j]:
                # Return the duplicate number
                return arr[i]
            j += 1

#optimize approach
def findDuplicate(arr, n) :
    seen = set() #initialise a set
    # Iterate through each element in the array
    for i in range(n): 
        #check wheather the element exists in the array
        if arr[i] in seen:
            #return the duplicate
            return arr[i]
        seen.add(arr[i]) # Add the unique element to the set

# Main
n = int(input())  # Number of elements in the array
arr = list(int(i) for i in input().strip().split(' '))  # Array of integers

# Call the duplicateNumber function
duplicate = duplicateNumber(arr, n)

# Print the duplicate number
print(duplicate)
