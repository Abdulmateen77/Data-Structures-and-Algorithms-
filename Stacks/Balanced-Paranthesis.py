from sys import stdin

def isBalanced(expression):
    # Function to check if the given expression is balanced or not
    stack = []  # Stack to store opening brackets

    for char in expression:
        if char in '[{(':  # If the character is an opening bracket
            stack.append(char)  # Push it onto the stack
        elif char is ')':  # If the character is a closing parenthesis
            if (not stack or stack[-1] != '('):  # If stack is empty or top of stack is not an opening parenthesis
                return False  # Return False (not balanced)
            stack.pop()  # Remove the corresponding opening parenthesis from the stack
        elif char is '}':  # If the character is a closing curly brace
            if (not stack or stack[-1] != '{'):  # If stack is empty or top of stack is not an opening curly brace
                return False  # Return False (not balanced)
            stack.pop()  # Remove the corresponding opening curly brace from the stack
        elif char is ']':  # If the character is a closing square bracket
            if (not stack or stack[-1] != '['):  # If stack is empty or top of stack is not an opening square bracket
                return False  # Return False (not balanced)
            stack.pop()  # Remove the corresponding opening square bracket from the stack

    if (not stack):  # If the stack is empty (all opening brackets are matched and removed)
        return True  # Return True (expression is balanced)
    else:
        return False  # Return False (expression is not balanced)


# main
expression = stdin.readline().strip()

if isBalanced(expression):
    print("true")  # Print "true" if the expression is balanced
else:
    print("false")  # Print "false" if the expression is not balanced
