def uniqueChar(s): 
    # Write your code here
    result = ""

    seen = set()

    for char in s:
        if char not in seen:
            result += char
            seen.add(char)
    
    return result








# Main 
s=input() 
print(uniqueChar(s))
