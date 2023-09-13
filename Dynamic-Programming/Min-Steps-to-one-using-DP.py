from sys import stdin
from sys import maxsize as MAX_VALUE


def countMinStepsToOne(n) :

    dp = [0] * (n+1)

    for i in range(2, n+1):
        miniSteps = 1 + dp[i -1]

        if i % 2 == 0:
           miniSteps = min(miniSteps, 1 + dp[i // 2])

        
        if i % 3 == 0:
            miniSteps = min(miniSteps, 1 + dp[i // 3])
        
        dp[i] = miniSteps
    
    return dp[n]

#main
n = int(stdin.readline().rstrip())
print(countMinStepsToOne(n))
