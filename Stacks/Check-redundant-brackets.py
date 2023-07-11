from sys import stdin

def checkRedundantBrackets(expression):
    stack = []  # Initialize an empty stack to store the characters

    for char in expression:
        if char == ')':
            top = stack.pop()  # Pop the top element from the stack
            isRedundant = True

            while top != '(':
                if top in '+-*/':
                    isRedundant = False  # If there is an operator between brackets, it is not redundant

                top = stack.pop()  # Continue popping elements until we find the opening bracket

            if isRedundant:
                return True  # If the brackets are redundant, return True

        else:
            stack.append(char)  # Push the character onto the stack

    return False  # If no redundant brackets are found, return False

# Main function
expression = stdin.readline().strip()

if checkRedundantBrackets(expression):
    print("true")
else:
    print("false")
