from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            # If the list is empty, return an empty string
            return ""
    # Find the minimum length among the strings
        min_len = min(len(s) for s in strs) 
        result = ""

        for i in range(min_len):
            current_char = strs[0][i]  # Get the current character from the first string

            # Check if the current character is the same in all strings
            if all(s[i] == current_char for s in strs):
                result += current_char
            else:
                break

        return result
