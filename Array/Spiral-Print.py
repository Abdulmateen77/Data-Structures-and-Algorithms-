from sys import stdin

def spiralPrint(mat, nRows, mCols):
    # Calculate the total number of elements in the matrix
    total = nRows * mCols
    count = 0

    # Initialize the indices
    startRow = 0
    endRow = nRows - 1
    startCol = 0
    endCol = mCols - 1
    
    while count < total:
        # Print elements from startRow to endCol
        inx = startRow
        while count < total and inx <= endCol:
            print(mat[startRow][inx], end=" ")
            count += 1
            inx += 1
        startRow += 1

        # Print elements from startRow+1 to endRow in endCol
        inx = startRow
        while count < total and inx <= endRow:
            print(mat[inx][endCol], end=" ")
            count += 1
            inx += 1
        endCol -= 1

        # Print elements from endRow to startCol in reverse order
        inx = endCol
        while count < total and inx >= startCol:
            print(mat[endRow][inx], end=" ")
            count += 1
            inx -= 1
        endRow -= 1

        # Print elements from endRow-1 to startRow in startCol in reverse order
        inx = endRow
        while count < total and inx >= startRow:
            print(mat[inx][startCol], end=" ")
            count += 1
            inx -= 1
        startCol += 1

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
    spiralPrint(mat, nRows, mCols)
    print()
    t -= 1
