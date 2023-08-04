class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0  # Initialize a count to track the number of necessary changes
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:  # If the current element is smaller than the previous one
                # Check if a change is already made or if it's possible to change this element
                if count or (i > 1 and i < len(nums) - 1 and nums[i-2] > nums[i] and nums[i+1] < nums[i-1]):
                    return False  # Return False if a change is not possible or already made
                count = 1  # Mark a change is made
            
        return True  # Return True if the array can be made non-decreasing
