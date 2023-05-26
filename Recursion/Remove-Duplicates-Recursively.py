# Problem, removeConsecutiveDuplicates
def removeConsecutiveDuplicates(string):
    # Base case: if the string is empty or contains only one character, return the string as it is
    if len(string) == 0 or len(string) == 1:
        return string
    
    # Recursive case: remove consecutive duplicates from the remaining part of the string
    smallOutput = removeConsecutiveDuplicates(string[1:])
    
    # Check if the current character is equal to the next character
    if string[0] == string[1]:
        # If they are equal, exclude the current character from the smallOutput
        return smallOutput
    else:
        # If they are not equal, include the current character in the result
        return string[0] + smallOutput


# Main
string = input().strip()  # Input the string and remove leading/trailing whitespaces
print(removeConsecutiveDuplicates(string))  # Print the string after removing consecutive duplicates
