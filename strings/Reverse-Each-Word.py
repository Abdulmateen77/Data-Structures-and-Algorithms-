from sys import stdin

def reverseWord(string, start, end):
    reverse = ""
    while start < end:
        reverse = string[start] + reverse  #Build the reverse word character by character
        start += 1
    return reverse

def reverseEachWord(string):
    n = len(string)
    previousSpaceIndex = -1
    ans = ""

    i = 0
    while i < n:
        if string[i] == ' ':
            ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")  # Reverse each word and add it to the result
            previousSpaceIndex = i
        i += 1

    ans += (reverseWord(string, previousSpaceIndex + 1, i) + " ")  # Reverse the last word and add it to the result

    return ans

# Main
string = stdin.readline().strip()  #Read the input string from standard input

ans = reverseEachWord(string)  #Call the reverseEachWord function to reverse each word in the string

print(ans)  #Print the reversed string with each word reversed
