import sys
def minStepsTo1(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):

        min_squares = float('inf')


        for j in range(1, int(i**0.5) + 1):
            square = j * j
            min_squares = min(min_squares, 1 + dp[i - square])

        dp[i] = min_squares

    return dp[n]
        

    
n = int(input())
ans = minStepsTo1(n)
print(ans)





