from sys import stdin

def findLargest(arr, nRows, mCols):
    # Initialize variables to store the maximum sum, row, and column
    Max_Row = float("-inf")
    Max_Col = float("-inf")
    row = -1
    col = -1

    #Find the largest row sum
    for i in range(nRows):
        row_sum = 0
        for j in range(mCols):
            row_sum += arr[i][j]
        if row_sum > Max_Row:
            Max_Row = row_sum
            row = i
    
    #Find the largest column sum
    for j in range(mCols):
        col_sum = 0
        for i in range(nRows):
            col_sum += arr[i][j]
        if col_sum > Max_Col:
            Max_Col = col_sum
            col = j

    #Compare the maximum row sum with the maximum column sum
    if Max_Row == float("-inf") and Max_Col == float("-inf"):
        print("row 0 -2147483648")
    elif Max_Row >= Max_Col:
        print("row", row, Max_Row)
    else:
        print("column", col, Max_Col)

#Function to take input for 2D matrix
def take2DInput():
    li = stdin.readline().rstrip().split(" ")
    nRows = int(li[0])
    mCols = int(li[1])
    
    if nRows == 0:
        return list(), 0, 0
    
    mat = [list(map(int, input().strip().split(" "))) for _ in range(nRows)]
    return mat, nRows, mCols

#Main function
t = int(stdin.readline().rstrip())

while t > 0:
    mat, nRows, mCols = take2DInput()
    findLargest(mat, nRows, mCols)
    t -= 1
