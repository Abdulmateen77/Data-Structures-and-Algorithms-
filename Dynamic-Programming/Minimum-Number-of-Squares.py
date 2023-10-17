#Import the sys module for system-related functions (not used in this code)
import sys

#Function to calculate the minimum steps to reach 1 using square numbers
def minStepsTo1(n):
    #Create a list to store the minimum steps for each number from 1 to n
    dp = [0] * (n + 1)

    #Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        # Initialize the minimum number of steps with a large value
        min_squares = float('inf')

        #Try all possible square numbers up to the current number 'i'
        for j in range(1, int(i**0.5) + 1):
            square = j * j
            # Update the minimum steps based on the current square number
            min_squares = min(min_squares, 1 + dp[i - square])

        # Store the minimum number of steps for the current number 'i' in the dp list
        dp[i] = min_squares

    # The minimum number of steps to reach 1 is stored in dp[n]
    return dp[n]

# Input: Read the integer 'n'
n = int(input())

# Calculate and print the minimum number of steps to reach 1 using square numbers
ans = minStepsTo1(n)
print(ans)
