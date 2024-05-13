#Define a function to calculate the Fibonacci number at position 'n'
def fib(n):
    
    #Base cases: Fibonacci numbers for n = 0 and n = -1
    if n == 0 or n == -1:
        return n
    #Check if the Fibonacci number for 'n' is already memoized
    elif n != [-1]:
        return memo[n]
    else:
        #Calculate the Fibonacci number for 'n' using recursion
        memo[n] = fib(n - 1) + fib(n - 2)
        return memo

# Check if the script is run as the main program
if __name__ == "__main__":
    # Get user input for the position 'n' of the desired Fibonacci number
    n = int(input())
    
    # Create a memoization table with -1 values for positions 0 to n-2
    memo = [-1] * (n - 1)
    
    # Print the nth Fibonacci number by calling the 'fib' function
    print("Nth fib number is: " + str(fib(n)))
