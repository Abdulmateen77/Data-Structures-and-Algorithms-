#Import specific modules needed.
from os import *
from sys import *
from collections import *
from math import *

# Dynamic programming function to solve the problem.
def solve(nums):
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

# Function to find the maximum sum of values in houses, ensuring no adjacent houses are robbed.
def houseRobber(valueInHouse):
    # Get the number of houses.
    n = len(valueInHouse)

    # If there is only one house, return its value as the result.
    if n == 1:
        return valueInHouse[0]

    # Create two separate lists 'first' and 'second' to consider two cases:
    # 1. Rob the first house and exclude the last one.
    # 2. Exclude the first house and consider all others.
    first = []
    second = []

    for i in range(n):
        if i != n - 1:
            first.append(valueInHouse[i])

        if i != 0:
            second.append(valueInHouse[i])

    # Return the maximum of the two cases using the 'solve' function.
    return max(solve(first), solve(second))
