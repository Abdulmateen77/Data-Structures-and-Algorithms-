from os import *
from sys import *
from collections import *
from math import *

dp = []

def miniPath(n, m, N, triangle):
    global dp
    if n == N-1:
        return triangle[n][m]

    if dp[n][m] != -1:
        return dp[n][m]
    
    dp[n][m] = min(miniPath(n+1,m,N,triangle), miniPath(n+1, m+1, N, triangle)) + triangle[n][m]

    return dp[n][m]

def minimumPathSum(triangle, n):
    # Write your code here.
    global dp

    dp = [[-1 for j in range(n)] for i in range(n)]

    return miniPath(0, 0, n, triangle)
