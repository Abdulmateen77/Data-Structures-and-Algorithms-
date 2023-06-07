from sys import stdin

def findTriplet(arr, n, x):
    count = 0  # Initialize a variable to count the number of triplets
    for i in range(n-1):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                # Check if the sum of the elements at indices i, j, and k is equal to x
                if arr[i] + arr[j] + arr[k] == x:
                    count += 1  # Increment the count if a triplet is found
    return count  # Return the count of triplets
