from sys import stdin

def pairSum0(l, n):
    sum = 0
    count = 0
    #Create a dictionary to store element frequencies
    map = {}
    for i in range(n):
        # Check if the complement of the current element (sum - l[i]) is in the map
        if map and sum - l[i] in map:
            count += map[sum - l[i]]  # Increment count by the frequency of the complement
        
        # Increment the frequency of the current element in the map
        if l[i] in map:
            map[l[i]] += 1
        else:
            map[l[i]] = 1
    
    return count

# Read input for the number of elements in the array
n = int(input())

# Read input array elements
arr = list(map(int, input().split()))

# Call the pairSum0 function and print the count of pairs with sum 0
result = pairSum0(arr, n)
print(result)

