def CountZeros(N):
    if N == 0:
        return 1  # Base case: If N is zero, return 1 since it is itself a zero
        
    if N < 10:
        return 0  # Base case: If N is a single digit number, return 0 (no zeros present)

    count = CountZeros(N // 10)  # Recursive call with the remaining digits of N
    if N % 10 == 0:
        count += 1  # If the last digit of N is zero, increment the count by 1
    return count

def main():
    N = int(input())  # Read the input integer N
    result = CountZeros(N)  # Call the CountZeros function to count the zeros in N
    print(result)  # Print the result

if __name__ == "__main__":
    main()
