from sys import stdin

#Brute Force Approach
def pairSum(arr, n, x):
    count = 0  # Initialize a variable to count the number of pairs
    for i in range(n-1):
        for j in range(i+1, n):
            # Check if the sum of the elements at indices i and j is equal to x
            if arr[i] + arr[j] == x:
                count += 1  # Increment the count if a pair is found
    return count  # Return the count of pairs


#Optimal Approach

def pairSum(arr, n, num):
# Function to count the number of pairs with a given sum in an array
# arr: input array
# n: length of the array
# num: target sum

num_dict = {}  # Dictionary to store the frequency of array elements
count = 0  # Variable to store the count of pairs

for i in range(n):
    # Calculate the complement of the current element
    complement = num - arr[i]  
    if complement in num_dict:
        # If the complement is present in the dictionary, increment the count by its frequency
        count += num_dict[complement]
    # Update the frequency of the current element
    num_dict[arr[i]] = num_dict.get(arr[i], 0) + 1 
return count
