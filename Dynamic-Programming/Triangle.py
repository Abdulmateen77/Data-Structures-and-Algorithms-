# Import necessary modules
from os import *
from sys import *
from collections import *
from math import *

# Initialize a global 2D array to store memoized results
dp = []

# Function to calculate the minimum path sum in a triangle
def miniPath(n, m, N, triangle):
    global dp
    if n == N - 1:
        return triangle[n][m]

    if dp[n][m] != -1:
        return dp[n][m]

    # Calculate the minimum path sum recursively by considering two possible paths
    dp[n][m] = min(miniPath(n + 1, m, N, triangle), miniPath(n + 1, m + 1, N, triangle)) + triangle[n][m]

    return dp[n][m]

# Main function to find the minimum path sum in a triangle
def minimumPathSum(triangle, n):
    global dp

    # Initialize the memoization (dp) array with -1
    dp = [[-1 for j in range(n)] for i in range(n)]

    # Call the miniPath function to find the minimum path sum
    return miniPath(0, 0, n, triangle)
