def printPairDiffK(arr, k):
    # Initialize an empty dictionary to store element frequencies
    dict = {}
    # Initialize a count to keep track of valid pairs
    count = 0

    # Loop through the elements in the list
    for num in arr:
        # Check if there exists an element that forms a pair with a difference of k
        if k != 0 and num - k in dict:
            # Increment the count by the frequency of the complement element
            count += dict[num - k]
        
        # Check if there exists an element that forms a pair with a difference of k
        if num + k in dict:
            # Increment the count by the frequency of the complement element
            count += dict[num + k]

        # Increment the frequency of the current element in the dictionary
        dict[num] = dict.get(num, 0) + 1

    # Return the total count of valid pairs
    return count 

# Main
# Read input for the number of elements in the list
n = int(input())
# Read the elements of the list
l = list(int(i) for i in input().strip().split(' '))
# Read input for the target difference k
k = int(input())
# Call the function and print the result
print(printPairDiffK(l, k))
