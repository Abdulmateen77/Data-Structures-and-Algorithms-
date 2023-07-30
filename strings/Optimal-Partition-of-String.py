class Solution:
    def partitionString(self, s: str) -> int:
        dictionary = {}
        count = 0

        for char in s:
            if (char in dictionary):
                count += 1
                dictionary = {}
                dictionary[char] = 1
            else:
                dictionary[char] = 1
        
        if len(dictionary) != 0:
            count +=1 
        
        return count
