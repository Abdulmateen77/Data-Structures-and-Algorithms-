from os import *
from sys import *
from collections import *
from math import *

from typing import *

dp = []

def f(n: int, heights: List[int], N:int) -> int:
    global dp 
    if n == N:
        return 0
    
    elif n == N-1:
        return abs(heights[N-1] - heights[N-2])
    if dp[n] != -1:
        return dp[n]
    else:
        dp[n] =  min(f(n+1,heights,N) + abs(heights[n-1]-heights[n]), f(n+2,heights,N) +abs(heights[n-1] - heights[n+1]))
        return dp[n]
         
def frogJump(n: int, heights: List[int]) -> int:
    global dp
    # Write your code here.
    dp = [-1] * (n+1)
    
    return f(1, heights, n)
