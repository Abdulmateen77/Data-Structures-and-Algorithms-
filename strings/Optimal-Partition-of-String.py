class Solution:
    def partitionString(self, s: str) -> int:
        dictionary = {}  # Create an empty dictionary to store characters seen in the current partition
        count = 0        # Initialize a count variable to keep track of the partitions

        for char in s:   # Iterate through each character in the input string
            if char in dictionary:
                count += 1                 # If the character is already present in the dictionary, it indicates the end of a partition
                dictionary = {}           # Reset the dictionary for the next partition
                dictionary[char] = 1      # Add the current character to the new partition dictionary
            else:
                dictionary[char] = 1      # If the character is not present in the dictionary, add it to the current partition

        if len(dictionary) != 0:
            count += 1   # If there are any remaining characters in the dictionary after the loop, add one more partition

        return count     # Return the total number of partitions

def main():
    # Test case 1
    solution = Solution()
    s1 = "abacab"
    result1 = solution.partitionString(s1)
    print(f"Number of partitions for '{s1}': {result1}")  # Expected output: 3

    # Test case 2
    s2 = "xyz"
    result2 = solution.partitionString(s2)
    print(f"Number of partitions for '{s2}': {result2}")  # Expected output: 3

    # Test case 3
    s3 = "aabaa"
    result3 = solution.partitionString(s3)
    print(f"Number of partitions for '{s3}': {result3}")  # Expected output: 2

if __name__ == "__main__":
    main()
