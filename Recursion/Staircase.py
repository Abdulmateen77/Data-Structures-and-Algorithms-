def staircase(n):
    """
    Recursive function to calculate the number of ways to climb a staircase with n steps.
    """
    if n <= 0:
        return 0  # The base case should return 0 instead of 1, as there are no steps to climb
    elif n == 1:
        return 1  # There is only one way to climb 1 step
    elif n == 2:
        return 2  # There are two ways to climb 2 steps: (1, 1) or (2)
    elif n == 3:
        return 4  # There are four ways to climb 3 steps: (1, 1, 1), (1, 2), (2, 1), or (3)
    else:
        # For any n > 3, recursively calculate the number of ways by considering the three possibilities:
        # (1) Taking one step and considering the remaining n-1 steps
        # (2) Taking two steps and considering the remaining n-2 steps
        # (3) Taking three steps and considering the remaining n-3 steps
        return staircase(n - 1) + staircase(n - 2) + staircase(n - 3)


def main():
    """
    Main function to get user input and print the number of ways to climb the staircase.
    """
    n = int(input("Enter the number of steps: "))  # Get the number of steps from the user
    print("The number of ways to run up the staircase is:", staircase(n))


if __name__ == "__main__":
    main()
