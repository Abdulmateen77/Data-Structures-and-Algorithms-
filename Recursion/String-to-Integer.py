def StringToInteger(string):
    # Get the size of the string
    size = len(string)
    
    # Base case: If the size is 1, convert the string to an integer and return it
    if size == 1:
        return int(string)
    
    # Convert the last digit of the string to an integer
    lastDigit = int(string[size-1])

    # Get the remaining part of the string (excluding the last digit)
    remaining = string[:size-1]
    
    # Recursive call: Convert the remaining string to an integer and multiply it by 10
    # Then add the last digit to the result
    return StringToInteger(remaining) * 10 + lastDigit
    
def main():
    # Read the input string
    string = input()
    
    # Convert the string to an integer using the StringToInt function
    result = StringToInteger(string)
    
    # Print the result
    print(result)

if __name__ == "__main__":
    main()
