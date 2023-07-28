class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Initialize count and MajorityEle variables
        count = 0
        MajorityEle = 0

        # Loop through each element in the given list
        for num in nums:
            # When the count becomes zero, update MajorityEle with the current element
            if count == 0:
                MajorityEle = num
            
            # If the current element is the same as the MajorityEle, increment the count
            if num == MajorityEle:
                count += 1
            # If the current element is different from MajorityEle, decrement the count
            else:
                count -= 1

        # Return the majority element found in the list
        return MajorityEle
