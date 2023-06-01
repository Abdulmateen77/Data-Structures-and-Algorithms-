def digitSum(N):
    # Base case: If N is less than 10, it's a single-digit number, so return N itself
    if N < 10:
        return N
    # Recursive case: Calculate the sum of the last digit of N and the sum of digits of the remaining number
    return N % 10 + digitSum(N // 10)


def main():
    # Read the input integer from the user
    N = int(input("Enter an integer: "))
    # Calculate the sum of digits using the digitSum function
    result = digitSum(N)
    # Print the result
    print("Sum of digits:", result)

if __name__ == "__main__":
    main()
