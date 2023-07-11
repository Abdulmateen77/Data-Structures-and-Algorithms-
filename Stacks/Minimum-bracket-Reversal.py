from sys import stdin

def countBracketReversals(expression):
    # Check if the length of the expression is odd, which would make it impossible to balance the brackets
    if len(expression) % 2 != 0:
        return -1

    stack = []  # Stack to store opening brackets
    unmatched_brackets = [0, 0]  # List to track unmatched brackets: [unmatched opening brackets, unmatched closing brackets]

    for ch in expression:
        if ch == "{":  # If the character is an opening bracket, push it to the stack
            stack.append(ch)
        else:
            if stack:  # If the stack is not empty, pop the top element (matching opening bracket)
                stack.pop()
            else:  # If the stack is empty, there is an unmatched closing bracket
                unmatched_brackets[0] += 1

    while stack:  # Check for any unmatched opening brackets remaining in the stack
        unmatched_brackets[1] += 1
        stack.pop()

    # Return the minimum number of reversals needed to balance the brackets
    return int((unmatched_brackets[0] + 1) / 2) + int((unmatched_brackets[1] + 1) / 2)

# Main
print(countBracketReversals(stdin.readline().strip()))
