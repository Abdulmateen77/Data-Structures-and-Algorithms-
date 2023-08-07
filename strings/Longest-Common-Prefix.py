from typing import List

class Solution:
    def __init__(self):
        pass  # You can initialize any instance variables here if needed
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        min_len = min(len(s) for s in strs)
        result = ""

        for i in range(min_len):
            current_char = strs[0][i]

            if all(s[i] == current_char for s in strs):
                result += current_char
            else:
                break

        return result

def main():
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test your longestCommonPrefix function
    input_strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(input_strs)
    print("Longest Common Prefix:", result)  # Expected output: "fl"

if __name__ == "__main__":
    main()
