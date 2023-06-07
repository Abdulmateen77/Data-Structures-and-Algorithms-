from sys import stdin


def pairSum(arr, n, x):
    count = 0  # Initialize a variable to count the number of pairs
    for i in range(n-1):
        for j in range(i+1, n):
            # Check if the sum of the elements at indices i and j is equal to x
            if arr[i] + arr[j] == x:
                count += 1  # Increment the count if a pair is found
    return count  # Return the count of pairs
