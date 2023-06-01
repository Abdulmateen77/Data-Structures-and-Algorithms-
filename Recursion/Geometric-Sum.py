def GeometricSum(k):
    # Base case: when k reaches 0, return 1
    if k == 0:
        return 1
    else:
        # Recursive case: calculate the current term as 1/(2^k)
        # and add it to the sum of the previous terms
        return 1 / (2 ** k) + GeometricSum(k - 1)

def main():
    # Read the number of terms to sum from user input
    k = int(input())

    # Calculate the geometric sum using the GeometricSum function
    result = GeometricSum(k)

    # Print the result with 5 decimal places
    print("{:.5f}".format(result))

if __name__ == "__main__":
    main()
