# Function to print a 2D array
def print2DArray(mat, rows, cols):
    # Iterate through each row of the matrix
    for i in range(rows):
        n = rows - i
        # Print each element in the row
        while n != 0:
            for j in range(cols):
                print(mat[i][j], end=' ')
            n -= 1  # Decrement the counter for the row
            print()  # Move to the next line after printing a row

# Main
mat = []  # Initialize an empty list to store the matrix

# Read the dimensions of the matrix from user input
li = input().strip().split()
rows = int(li[0])  # Number of rows in the matrix
cols = int(li[1])  # Number of columns in the matrix

# Read the matrix elements row by row and append them to the matrix
for i in range(rows):
    row = [int(elem) for elem in list(input().strip().split())]
    mat.append(row)

# Call the print2DArray function to print the matrix
print2DArray(mat, rows, cols)
