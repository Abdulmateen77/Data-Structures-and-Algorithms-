class Solution:
    def fib(self, n: int) -> int:
        # Base cases:
        # If n is 0, return 0
        if n == 0:
            return 0
        # If n is 1 or 2, return 1
        elif n == 1 or n == 2:
            return 1
        # Recursive call to calculate the Fibonacci number
        return self.fib(n-1) + self.fib(n-2) 

def main():
    # Read the input value for n
    n = int(input())

    # Create an instance of the Solution class
    solution = Solution()

    # Calculate the Fibonacci number using the fib method
    result = solution.fib(n)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
