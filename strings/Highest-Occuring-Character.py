from sys import stdin

def highestOccuringChar(string):
    n = len(string)
    frequency = [0] * 256  #Initialize an array to store the frequency of each character
    maxFrequency = 0

    #Count the frequency of each character in the string
    for i in range(n):
        frequency[ord(string[i])] += 1  # Increment the frequency count for the character
        maxFrequency = max(maxFrequency, frequency[ord(string[i])])  # Update the max frequency

    answer = '0'
    
    #Find the character with the highest frequency
    for i in range(n):
        if frequency[ord(string[i])] == maxFrequency:
            answer = string[i]  # Update the answer with the current character
            break  # Exit the loop since we have found the character

    return answer

#Main
string = stdin.readline().strip()  # Read the input string from standard input

ans = highestOccuringChar(string)  # Call the highestOccuringChar function

print(ans)  # Print the character with the highest occurrence in the string
