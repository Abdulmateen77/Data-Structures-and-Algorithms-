def solution(A, B, X, Y):
    N = len(A)

    # Create a matrix to store the minimum time to reach each position on both lines
    dp = [[float('inf')] * 2 for _ in range(N)]

    # Initialize the first position on both lines
    dp[0][0] = A[0]
    dp[0][1] = B[0]

    # Fill in the matrix based on the minimum time to reach each position
    for i in range(1, N):
        dp[i][0] = min(dp[i-1][0] + A[i], dp[i-1][1] + A[i] + Y)
        dp[i][1] = min(dp[i-1][1] + B[i], dp[i-1][0] + B[i] + X)

    # Return the minimum time to assemble the entire car
    return min(dp[N-1][0], dp[N-1][1])

# Examples:
result1 = solution([1, 6, 2], [3, 2, 5], 2, 1)
result2 = solution([2, 11, 4, 4], [9, 2, 5, 11], 8, 4)
result3 = solution([1, 10, 1], [10, 1, 10], 1, 5)
result4 = solution([8, 3, 3], [6, 1, 10], 4, 3)

print(result1)  # Output: 8
print(result2)  # Output: 21
print(result3)  # Output: 9
print(result4)  # Output: 13
