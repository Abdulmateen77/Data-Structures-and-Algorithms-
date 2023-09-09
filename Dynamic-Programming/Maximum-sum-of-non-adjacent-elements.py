# Import specific modules you need.
from sys import stdin

# Dynamic programming function to solve the problem.
def solveTab(nums):
    n = len(nums)

    # Initialize a dynamic programming (DP) array of length 'n'.
    dp = [0] * (n)

    # Set the initial DP value for the first element of 'nums'.
    dp[0] = nums[0]

    # Iterate through the array 'nums' starting from the second element.
    for i in range(1, n):
        # Calculate the maximum sum including the current element ('incl').
        incl = dp[i - 2] + nums[i]

        # Calculate the maximum sum excluding the current element ('excl').
        excl = dp[i - 1] + 0  # Excluding the current element means taking the previous sum.

        # Store the maximum of 'incl' and 'excl' in the DP array.
        dp[i] = max(incl, excl)

    # Return the maximum sum stored in the last element of the DP array.
    return dp[n - 1]

# Function to find the maximum sum of non-adjacent elements in an array.
def maximumNonAdjacentSum(nums):
    # Call the dynamic programming function to solve the problem.
    return solveTab(nums)

# Main function to read input and process test cases.
t = int(stdin.readline().rstrip())

while t > 0:
    # Read the size of the array.
    n = int(stdin.readline().rstrip())

    # Read the array of integers and split them by spaces.
    arr = list(map(int, stdin.readline().rstrip().split(" ")))

    # Call the function to find the maximum non-adjacent sum and print the result.
    print(maximumNonAdjacentSum(arr))

    t -= 1
