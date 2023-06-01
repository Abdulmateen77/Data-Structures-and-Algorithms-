import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert the input string to lowercase
        s = s.lower()
        
        # Remove non-alphanumeric characters using regex substitution
        s = re.sub(r'[^a-z0-9]', '', s)
        
        # Get the size of the cleaned string
        size = len(s)
        
        # Call the recursive helper function to check if it is a palindrome
        return self.isPalindromeRecursive(s, 0, size-1)
    
    def isPalindromeRecursive(self, string, left, right):
        # Base case: When left pointer surpasses the right pointer,
        # it means we have checked all characters and it is a palindrome
        if left >= right:
            return True
        
        # Recursive case: If the characters at the left and right pointers are equal,
        # move the pointers inward and continue checking the remaining characters
        if string[left] == string[right]:
            return self.isPalindromeRecursive(string, left + 1, right - 1)
        else:
            return False
