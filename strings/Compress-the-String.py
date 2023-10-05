# Import the sys module to access standard input (stdin) and setrecursionlimit to increase recursion depth
from sys import stdin, setrecursionlimit

# Set the recursion depth limit to 10^7 to prevent stack overflow (may be needed for large inputs)
setrecursionlimit(10**7)

# Define a function called getCompressedString that takes an input string and returns a compressed version
def getCompressedString(input):
    n = len(input)  # Calculate the length of the input string
    
    if n == 0:  # If the input string is empty, return an empty string
        return ""
    
    startChr = 0  # Initialize a variable 'startChr' to point to the first character of the string
    endChr = 0    # Initialize a variable 'endChr' to point to the first character of the string
    output = ""   # Initialize an empty string 'output' to store the compressed result
    
    while startChr < n:  # Start a loop that iterates through the input string
        while endChr < n and input[endChr] == input[startChr]:
            endChr += 1  # Move 'endChr' to the right while the characters are the same
        
        totalChrCount = endChr - startChr  # Calculate the count of consecutive characters
        
        if totalChrCount > 1:  # If there are more than one consecutive characters
            output += input[startChr] + str(totalChrCount)  # Append character and its count to 'output'
        else:
            output += input[startChr]  # Otherwise, append the character itself to 'output'
        
        startChr = endChr  # Move 'startChr' to the position where 'endChr' stopped
    
    return output  # Return the compressed string

# Main program starts here

# Read a line of input from standard input (stdin) and remove leading/trailing whitespace
string = stdin.readline().strip()

# Call the getCompressedString function to get the compressed version of the input string
ans = getCompressedString(string)

# Print the compressed string
print(ans)
