class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Rotate the elements of the given 'nums' list to the right by 'k' positions.
        
        Parameters:
        - nums (List[int]): The input list of integers to be rotated.
        - k (int): The number of positions to rotate the list to the right.
        
        Returns:
        - None: The function modifies 'nums' in-place and does not return a new list.
        """
        n = len(nums)
        
        # If 'k' is greater than the length of the array, reduce it to the equivalent rotation within the array length
        if n < k:
            k = k % n
        
        # Rotate the array in-place by concatenating the subarrays
        nums[:] = nums[n - k:] + nums[:n - k]
        
        # No need to return 'nums' since the modification is done in-place
