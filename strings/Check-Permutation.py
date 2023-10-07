def isPermutation(string1, string2):
    if len(string1) != len(string2):  #Check if the lengths of the strings are different
        return False  #If the lengths are different, they cannot be permutations of each other
    
    chr1 = list(string1)  #Convert string1 to a list of characters
    chr2 = list(string2)  #Convert string2 to a list of characters

    chr1.sort()  #Sort the characters in string1
    chr2.sort()  #Sort the characters in string2

    for i in range(0, len(chr1)):
        if chr1[i] != chr2[i]:  #Compare the characters at corresponding positions
            return False  #If any pair of characters are different, they are not permutations
    
    return True  #If the loop completes without finding any unequal characters, they are permutations
