class Solution:
    
    def lengthOfLastWord(self, s: str) -> int:
        #Function to calculate the length of the last word in a string.

        last = 0  #Variable to store the length of the last word.
        s = s.strip()  #Remove leading and trailing whitespaces from the string.
        i = len(s) - 1  #Start from the last character of the string.

        while i >= 0:
            #Iterate backwards through the string until a whitespace or the beginning of the string is encountered.

            if s[i] == " ":
                #If a whitespace is encountered, it means the last word has ended, so break the loop.
                break

            i -= 1  #Move to the previous character.
            last += 1  #Increment the length of the last word.

        return last  #Return the length of the last word.
