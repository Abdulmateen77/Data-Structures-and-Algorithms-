def power(x, n):
    # Base case: any number raised to the power of 0 is 1
    if n == 0:
        return 1

    # Recursive case for positive n
    if n > 0:
        small_power = power(x, n // 2)
        if n % 2 == 0:
            return small_power * small_power
        else:
            return x * small_power * small_power

    # Recursive case for negative n
    if n < 0:
        small_power = power(x, -n)
        return 1 / small_power


# Main
from sys import setrecursionlimit
setrecursionlimit(11000)
x, n=list(int(i) for i in input().strip().split(' '))
print(power(x, n))
