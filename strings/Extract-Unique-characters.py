def uniqueChar(s):
    # Initialize an empty string to store the result
    result = ""
    # Create a set to keep track of characters that have been encountered
    seen = set()
    # Iterate through each character in the input string 's'
    for char in s:
        # Check if the character is not already encountered
        if char not in seen:
            # Add the character to the result string
            result += char
            # Add the character to the set to mark it as seen
            seen.add(char)
    
    # Return the resulting string containing unique characters
    return result


# Main 
# Read input from the user
s = input()
# Call the uniqueChar function and print the result
print(uniqueChar(s))
