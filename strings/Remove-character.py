from sys import stdin

def removeAllOccurrencesOfChar(string, ch):
    new_string = ""
    for i in range(len(string)):
        if string[i] == ch:
            pass  # Skip adding the character to the new string
        else:
            new_string += string[i]  # Add the character to the new string
    return new_string

# Main
string = stdin.readline().strip()  # Read the input string from standard input
ch = stdin.readline().strip()  # Read the character to be removed from standard input

ans = removeAllOccurrencesOfChar(string, ch)  # Call the removeAllOccurrencesOfChar function

print(ans)  # Print the modified string with the specified character removed
