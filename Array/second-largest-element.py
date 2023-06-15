class Solution:
    def print2largest(self, arr, n):
        arr.sort()  # Sort the array in ascending order
        max_num = arr[-1]  # Get the maximum number from the array

        for i in arr[::-1]:  # Iterate the array in reverse order
            if max_num == i:
                continue  # Skip the maximum number
            elif max_num > i:
                return i  # Return the second largest number

        return -1  # If no second largest number found, return -1
