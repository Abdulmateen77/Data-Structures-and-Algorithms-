# Import necessary module for reading input
from sys import stdin

# Import a constant representing the maximum integer value
from sys import maxsize as MAX_VALUE

# Function to calculate the minimum steps to reduce 'n' to 1
def countMinStepsToOne(n):
    # Create a list to store the minimum steps for each number from 1 to n
    dp = [0] * (n + 1)

    # Iterate through the numbers from 2 to n
    for i in range(2, n + 1):
        # Initialize the minimum steps with 1 plus the minimum steps for (i-1)
        miniSteps = 1 + dp[i - 1]

        # Check if (i-1) is divisible by 2 and update the minimum steps accordingly
        if i % 2 == 0:
            miniSteps = min(miniSteps, 1 + dp[i // 2])

        # Check if (i-1) is divisible by 3 and update the minimum steps accordingly
        if i % 3 == 0:
            miniSteps = min(miniSteps, 1 + dp[i // 3])

        # Store the minimum steps in the dp list for the current number 'i'
        dp[i] = miniSteps

    # The minimum steps to reduce 'n' to 1 is stored in dp[n]
    return dp[n]

# Main function
# Read the input 'n'
n = int(stdin.readline().rstrip())
# Call the function to calculate minimum steps
result = countMinStepsToOne(n)
# Print the result
print(result)                        

# Note: The code reads 'n' from input, calculates the minimum steps, and prints the result.
