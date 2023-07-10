from sys import stdin

def wavePrint(mat, nRows, mCols):
    # Loop through each column of the matrix
    col = 0
    while col < mCols:
        # Print elements in the column from bottom to top if the column number is odd
        if col % 2 != 0:
            row = nRows - 1
            while row >= 0:
                print(mat[row][col], end=" ")
                row -= 1
        # Print elements in the column from top to bottom if the column number is even
        else:
            row = 0
            while row < nRows:
                print(mat[row][col], end=" ")
                row += 1
        col += 1

# Function to take input for 2D matrix
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0:
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for _ in range(nRows)]
    return mat, nRows, mCols

# Main function
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    wavePrint(mat, nRows, mCols)
    print()
    t -= 1
