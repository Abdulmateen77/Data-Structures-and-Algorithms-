class Solution:
    def print2largest(self, arr, n):
        first = -1  # Initialize the first largest element as -1
        second = -1  # Initialize the second largest element as -1

        for i in range(len(arr)):
            if arr[i] > first:
                second = first  # Update the second largest element to the previous first largest element
                first = arr[i]  # Update the first largest element
            elif arr[i] > second and arr[i] != first:
                second = arr[i]  # Update the second largest element

        return second  # Return the second largest element

#better approach
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
