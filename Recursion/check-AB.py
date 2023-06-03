def CheckAB(string):
    # Base case: if the string is empty, return "true"
    if len(string) == 0:
        return "true"

    # If the first character is 'a'
    if string[0] == 'a':
        # Recursively check if the remaining string (excluding the first character) satisfies the rules,
        # or check if appending "bb" to the remaining string satisfies the rules
        return CheckAB(string[1:]) or CheckAB(string[1:] + "bb")
    
    # If the first two characters are "bb", recursively check if the remaining string (excluding the first two characters) satisfies the rules
    elif string[0:2] == "bb":
        return CheckAB(string[2:])
    
    # If none of the above conditions match, return "false"
    else:
        return "false"


def main():
    # Read the input value for the string
    string = input()

    # Call the CheckAB function to check the string
    result = CheckAB(string)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()
