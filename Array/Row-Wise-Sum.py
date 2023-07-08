from sys import stdin

def rowWiseSum(mat, nRows, mCols):
    # Iterate over each row
    for i in range(nRows):
        sum = 0
        # Iterate over each element in the row
        for j in range(mCols):
            # Calculate the sum of elements in the row
            sum += mat[i][j]
        # Print the sum for the current row
        print(sum, end=" ")

# Function to take input for 2D matrix
def take2DInput():
    # Read the dimensions of the matrix
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    # If matrix has 0 rows, return an empty list and 0 dimensions
    if nRows == 0:
        return list(), 0, 0
    
    # Read the elements of the matrix row-wise
    mat = [list(map(int, input().strip().split(" "))) for row in range(nRows)]
    return mat, nRows, mCols

# Main function
t = int(stdin.readline().rstrip())

while t > 0:
    # Take input for each test case
    mat, nRows, mCols = take2DInput()
    # Calculate and print the row-wise sums
    rowWiseSum(mat, nRows, mCols)
    print()

    t -= 1
