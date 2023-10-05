# Import the sys module to access standard input (stdin)
from sys import stdin

# Define a function called isPalindrome that checks if a given string is a palindrome
def isPalindrome(string):
    left = 0               # Initialize a variable 'left' to point to the first character of the string
    right = len(string) - 1  # Initialize a variable 'right' to point to the last character of the string
    
    # Use a while loop to compare characters from both ends of the string
    while left < right:
        if string[left] != string[right]:  # If characters at 'left' and 'right' positions are different
            return False                  # Return False, indicating it's not a palindrome
        
        left += 1  # Move 'left' one position to the right
        right -= 1  # Move 'right' one position to the left
    
    return True  # If the loop completes without returning False, the string is a palindrome, so return True

# Main program starts here

# Read a line of input from standard input (stdin) and remove leading/trailing whitespace
string = stdin.readline().strip()

# Call the isPalindrome function to check if the input string is a palindrome
ans = isPalindrome(string)

# Check the result of isPalindrome function and print the appropriate message
if ans:
    print('true')  # If it's a palindrome, print 'true'
else:
    print('false')  # If it's not a palindrome, print 'false'
