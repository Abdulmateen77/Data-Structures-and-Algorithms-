# Define a class Solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Define a helper function to expand around the center of a palindrome
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        
        # Initialize an empty string to store the longest palindrome
        longest = ""
        
        # Iterate through each character in the input string 's'
        for i in range(len(s)):
            # Find the longest odd-length palindrome with the center at 'i'
            odd_palindrome = expand_around_center(i, i)
            
            # Find the longest even-length palindrome with the centers at 'i' and 'i+1'
            even_palindrome = expand_around_center(i, i + 1)
            
            # Update 'longest' with the longer palindrome between odd and even
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome
            if len(even_palindrome) > len(longest):
                longest = even_palindrome
        
        # Return the longest palindrome found
        return longest
