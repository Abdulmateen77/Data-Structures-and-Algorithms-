from os import *
from sys import *
from collections import *
from math import *

from sys import stdin

def solveTab(nums):

    n = len(nums)

    dp = [0] * (n)

    dp[0] = nums[0]

    for i in range(1,n):
        incl = dp[i-2] + nums[i]
        excl = dp[i-1] + 0
        dp[i] = max(incl,excl)

    return dp[n-1]
def maximumNonAdjacentSum(nums):    
    # Write your code here.

    return solveTab(nums)



# Main.
t = int(stdin.readline().rstrip())

while t > 0:
    
    n = int(stdin.readline().rstrip())
    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    print(maximumNonAdjacentSum(arr))
    
    t -= 1
