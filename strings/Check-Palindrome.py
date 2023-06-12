from sys import stdin

def isPalindrome(string):
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] != string[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

# Main
string = stdin.readline().strip()  # Read the input string from standard input

ans = isPalindrome(string)  # Call the isPalindrome function to check if the string is a palindrome

if ans:
    print('true')  # Print 'true' if the string is a palindrome
else:
    print('false')  # Print 'false' if the string is not a palindrome
