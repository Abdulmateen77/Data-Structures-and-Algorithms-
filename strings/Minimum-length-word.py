# Read a string from user input
input_str = input()

# Initialize variables to keep track of the minimum length and corresponding string
min_len = len(input_str)
min_str = input_str

# Initialize a temporary string to store the current word
curr_str = ""

# Loop through each character in the input string
for char in input_str:
    # Check if the character is a space
    if char == " ":
        # If the length of the current word is shorter than the minimum length seen so far
        if len(curr_str) < min_len:
            # Update the minimum length
            min_len = len(curr_str)
            # Update the corresponding string
            min_str = curr_str
        # Reset the current word
        curr_str = ""
    else:
        # If the character is not a space, append it to the current word
        curr_str += char

# Check the length of the last word in case it's the shortest
if len(curr_str) < min_len:
    # Update the minimum length
    min_len = len(curr_str)
    # Update the corresponding string
    min_str = curr_str

# Print the shortest word
print(min_str)
