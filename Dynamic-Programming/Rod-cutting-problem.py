# Import necessary modules
from sys import stdin
import sys

# Function to calculate the maximum cost by cutting a rod of length 'n'
def cutRod(price, n):
    # Initialize a list to store the maximum cost for each rod length
    cost = [0 for i in range(n+1)]

    # The cost for a rod of length 0 is 0
    cost[0] = 0

    # Iterate through each possible rod length from 1 to 'n'
    for i in range(1, n+1):
        maxCost = -sys.maxsize-1  # Initialize the maximum cost as a very small value

        # Try all possible ways of cutting the rod and find the maximum cost
        for j in range(i):
            maxCost = max(maxCost, price[j] + cost[i-j-1])

        # Store the maximum cost for the current rod length 'i'
        cost[i] = maxCost

    # The maximum cost for a rod of length 'n' is stored in cost[n]
    return cost[n]

# Function to take input using fast I/O
def takeInput():
    n = int(input())  # Read the number of test cases

    # Read the price list for each test case
    price = list(map(int, input().strip().split(" ")))

    return price, n

# Main function
t = int(input())  # Read the number of test cases
while t:
    price, n = takeInput()  # Read input for each test case
    print(cutRod(price, n))  # Calculate and print the maximum cost
    t = t - 1  # Decrement the number of test cases

# calculates the maximum cost using the cutRod function, and prints the result.
