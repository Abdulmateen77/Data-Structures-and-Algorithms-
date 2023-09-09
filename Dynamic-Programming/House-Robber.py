from os import *
from sys import *
from collections import *
from math import *


def solve(nums):

    n = len(nums)

    dp = [0] * (n)

    dp[0] = nums[0]

    for i in range(1,n):
        incl = dp[i-2] + nums[i]
        excl = dp[i-1] + 0
        dp[i] = max(incl,excl)

    return dp[n-1]

def houseRobber(valueInHouse):
    # Write your function here.
    n = len(valueInHouse)

    if n == 1:
        return valueInHouse[0]
    
    first = []
    second = []

    for i in range(n):
        if i != n-1:
            first.append(valueInHouse[i])
        
        if i != 0:
            second.append(valueInHouse[i])

    
    return max(solve(first),solve(second))
