# Problem: Remove x from string
def removeX(string): 
    # Base case: if the string is empty, return the empty string
    if len(string) == 0:
        return string
    
    # Recursive case: remove 'x' from the remaining part of the string
    modifiedStr = removeX(string[1:])
    
    # Check if the first character is 'x'
    if string[0] == "x":
        # If it is 'x', exclude it from the modified string
        return modifiedStr
    else:
        # If it is not 'x', include it in the modified string
        return string[0] + modifiedStr

# Main
string = input()  # Input the string
print(removeX(string))  # Print the modified string without 'x'
