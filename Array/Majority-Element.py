class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        MajorityEle = 0

        for num in nums:
            if count == 0:
                MajorityEle = num
            
            if num == MajorityEle:
                count += 1
            else:
                count -= 1
        return MajorityEle
