from sys import stdin
import sys


def cutRod(price, n):

    # Write your code here
    cost = [0 for i in range(n+1)]

    cost[0] = 0

    for i in range(1, n+1):
        maxCost = -sys.maxsize-1

        for j in range(i):
            maxCost = max(maxCost, price[j] + cost[i-j-1])

        cost[i] = maxCost

    return cost[n] 











# Taking input using fast I/O.
def takeInput():
    n = int(input())

    price = list(map(int, input().strip().split(" ")))

    return price, n


# Main.
t = int(input())
while t:
    price, n = takeInput()
    print(cutRod(price, n))
    t = t-1
