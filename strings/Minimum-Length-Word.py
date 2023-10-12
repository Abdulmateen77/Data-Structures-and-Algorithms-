def minimumLengthWord():
    str = input()  #Read the input string

    min_len = len(str)  #Initialize the minimum length to the length of the input string
    min_str = str  # Initialize the minimum string to the input string

    curr_str = " "  # Initialize the current word string

    for char in str:
        if char == " ":
            if len(curr_str) < min_len:
                min_len = len(curr_str)  # Update the minimum length
                min_str = curr_str  # Update the minimum string
            curr_str = " "  # Reset the current word string
        else:
            curr_str = curr_str + char  # Append the character to the current word string

    if len(curr_str) < min_len:
        min_len = len(curr_str)  # Update the minimum length
        min_str = curr_str  # Update the minimum string

    print(min_str)  # Print the shortest word

# Call the function to execute the code
minimumLengthWord()
