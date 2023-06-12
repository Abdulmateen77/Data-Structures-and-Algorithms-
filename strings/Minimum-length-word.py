input_str = input()  # Avoid using "str" as a variable name since it shadows the built-in str type
min_len = len(input_str)
min_str = input_str

curr_str = ""

for char in input_str:
    if char == " ":
        if len(curr_str) < min_len:  # Correct the variable name and the comparison condition
            min_len = len(curr_str)  # Correct the variable name
            min_str = curr_str
        curr_str = ""
    else:
        curr_str += char

if len(curr_str) < min_len:  # Correct the variable name and the comparison condition
    min_len = len(curr_str)  # Correct the variable name
    min_str = curr_str

print(min_str)
