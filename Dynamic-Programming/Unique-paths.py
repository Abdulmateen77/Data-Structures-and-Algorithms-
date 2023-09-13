# Function to check if a given position (n, m) is valid in the matrix
def isValid(n, m, mat):
    N = len(mat)
    M = len(mat[0])

    # Check if n or m are out of bounds or if the element is marked as -1
    if n < 0 or n >= N or m < 0 or m >= M or mat[n][m] == -1:
        return False
    return True

# Initialize a global 2D array to store memoized results
dp = []

# Function to count unique paths from (0, 0) to (N-1, M-1) in a matrix
def Unique(n, m, N, M, mat):
    global dp
    if n == N - 1 and m == M - 1:
        return 1

    if dp[n][m] != -1:
        return dp[n][m]

    mod = 1000000007
    ans = 0

    # Check and count paths to the right (m+1) if it's a valid move
    if isValid(n, m + 1, mat):
        ans += Unique(n, m + 1, N, M, mat)

    # Check and count paths downward (n+1) if it's a valid move
    if isValid(n + 1, m, mat):
        ans += Unique(n + 1, m, N, M, mat)

    ans %= mod
    dp[n][m] = ans
    return ans

# Main function to calculate unique paths in a maze with obstacles
def mazeObstacles(n, m, mat):
    global dp
    dp = [[-1 for j in range(m)] for i in range(n)]

    # Call the Unique function to find the unique paths
    return Unique(0, 0, n, m, mat)
