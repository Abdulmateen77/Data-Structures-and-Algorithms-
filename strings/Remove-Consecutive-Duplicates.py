def removeConsecutiveDuplicates(string):
    new_string = ""  #Initialize an empty string to store the modified string
    current_char = string[0]  #Get the first character of the input string
    new_string += current_char  #Add the first character to the new string
    
    for i in range(1, len(string)):  #Iterate over the remaining characters of the input string
        if string[i] == current_char:  #If the current character is the same as the previous character
            pass  # Skip adding it to the new string (removing consecutive duplicates)
        else:
            new_string += string[i]  # Add the current character to the new string
        current_char = string[i]  # Update the current character
    
    return new_string  # Return the modified string
