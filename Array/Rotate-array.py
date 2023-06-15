class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # If k is greater than the array length, reduce it to the equivalent rotation within the array length
        if n < k:
            k = k % n
        
        # Rotate the array in-place by concatenating the subarrays
        nums[:] = nums[n - k:] + nums[:n - k]
        
        # No need to return nums since the modification is done in-place
