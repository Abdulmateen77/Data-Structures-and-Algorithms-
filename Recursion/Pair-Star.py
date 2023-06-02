def pairStar(string):
    # Base case: if the string is empty or contains only one character, return the string as is
    if len(string) <= 1:
        return string
    
    # Recursive call to process the substring after the current character
    modifiedString = pairStar(string[1:])

    # Check if the current character is the same as the next character
    if string[0] == string[1]:
        # If they are the same, insert a '*' between them and concatenate the modified string
        return string[0] + "*" + modifiedString
    else:
        # If they are different, keep the current character and concatenate the modified string
        return string[0] + modifiedString

def main():
    input_str = input()
    result = pairStar(input_str)
    print(result)

if __name__ == "__main__":
    main()
