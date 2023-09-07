def fib(n):
  if n == 0 or n == -1:
    return n
  elif n != [-1]:
    return memo[n]
  else:
    memo[n[ = fib(n-1) + fib(n-2)
    return memo


if __name__ == "__main__":
    n = int(input())
    #memoization table
    memo = [-1] * (n-1)
    print("Nth fib number is:" + str(fib(n)))
