def contains(s, t):
# Function to check if string t is a subsequence of string s
# s: the main string
# t: the subsequence to check
  
# Base cases: if t is empty, it is always a subsequence of s
if len(t) == 0:
    return True

# If s is empty and t is not empty, t cannot be a subsequence of s
if len(s) == 0:
    return False

# Check if the first characters of s and t match
if s[0] == t[0]:
    # Recursively check if the remaining parts of s and t are subsequences
    return contains(s[1:], t[1:])
else:
    # If the first characters don't match, skip the character in s
    return contains(s[1:], t)
s = input() # Read the main string from input
t = input() # Read the subsequence to check from input

ans = contains(s, t) # Call the contains function to check if t is a subsequence of s

if ans:
print('true') # Print 'true' if t is a subsequence of s
else:
print('false') # Print 'false' if t is not a subsequence of s
