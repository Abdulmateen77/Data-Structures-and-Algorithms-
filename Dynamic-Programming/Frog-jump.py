#Import specific modules and types you need.
from typing import List

#Global array to store dynamic programming results.
dp = []
#Recursive function to find the minimum cost to reach the end.
def findMin(n: int, heights: List[int], N: int) -> int:
    global dp

    #Base case: If we have reached the end, return 0.
    if n == N:
        return 0

    #Base case: If we are one step away from the end, return the absolute height difference.
    elif n == N - 1:
        return abs(heights[N - 1] - heights[N - 2])

    #If the result for the current step 'n' is already computed, return it.
    if dp[n] != -1:
        return dp[n]

    #Recursive cases:
    else:
        #Calculate the cost of jumping one step and add it to the result of the next step.
        jump_one_step = findMin(n + 1, heights, N) + abs(heights[n - 1] - heights[n])

        #Calculate the cost of jumping two steps and add it to the result of the step after that.
        jump_two_steps = findMin(n + 2, heights, N) + abs(heights[n - 1] - heights[n + 1])

        #Choose the minimum cost between jumping one step or two steps.
        dp[n] = min(jump_one_step, jump_two_steps)

        #Return the minimum cost for reaching the end from this step.
        return dp[n]

#Main function to calculate the minimum cost for the frog to reach the end.
def frogJump(n: int, heights: List[int]) -> int:
    global dp

    #Initialize the dynamic programming array with -1 values.
    dp = [-1] * (n + 1)

    #Start the recursion from the first step (index 1) and return the result.
    return findMin(1, heights, n)
