import sys

# Function to calculate multiplication recursively
def Multiplication(M, N):
    # Base case: if N is 0, return 0
    if N == 0:
        return 0

    # Recursively calculate the multiplication of M and N-1
    Calculate = Multiplication(M, N-1)

    # Add M to the calculated result
    return M + Calculate

# Main function
def main():
    # Read the input values for M and N
    M = int(input("Enter the first number: "))
    N = int(input("Enter the second number: "))

    # Set the recursion limit to a higher value
    sys.setrecursionlimit(10**6)

    # Calculate the multiplication using the Multiplication function
    result = Multiplication(M, N)

    # Print the result
    print("Multiplication:", result)

# Entry point of the program
if __name__ == "__main__":
    main()
