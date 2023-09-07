# Import specific modules you need, rather than using wildcard imports.
# These modules are not used in this code, so you can remove these import statements.
# from os import *
# from sys import *
# from collections import *
# from math import *

def countDistinctWays(nStairs: int) -> int:
    # Define a modulo constant for handling large numbers
    mod = 1000000007

    # Create an array 'dp' of length '2' with initial values '1'.
    dp = [1, 1]

    # Check if 'nStairs' is less than or equal to '1'.
    # Because in these cases, there is no need for further calculation,
    # and we can directly return the corresponding value from 'dp'.
    if nStairs <= 1:
        return dp[nStairs]

    # Iterate on the range '[2, nStairs]'.
    for currStep in range(2, nStairs + 1):

        # Calculate the number of ways to reach the 'currStep'th stair.
        currStepWays = (dp[0] + dp[1]) % mod

        # Update 'dp' array for the next iteration.
        dp[0] = dp[1]
        dp[1] = currStepWays

    # Return the number of distinct ways to reach the 'nStairs'th stair.
    return dp[1]
