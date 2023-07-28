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

def main():
    # Test Case 1
    nums1 = [3, 2, 3]
    sol1 = Solution()
    result1 = sol1.majorityElement(nums1)
    print("Majority Element in nums1:", result1)  # Output: 3

    # Test Case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    sol2 = Solution()
    result2 = sol2.majorityElement(nums2)
    print("Majority Element in nums2:", result2)  # Output: 2

    # Test Case 3
    nums3 = [1, 2, 2, 3, 2, 4, 2, 5, 2]
    sol3 = Solution()
    result3 = sol3.majorityElement(nums3)
    print("Majority Element in nums3:", result3)  # Output: 2

if __name__ == "__main__":
    main()
