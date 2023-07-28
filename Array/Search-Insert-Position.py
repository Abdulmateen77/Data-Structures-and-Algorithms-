from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Handle the edge case if the target is less than or equal to the first element
        if target <= nums[0]:
            return 0
        
        # Handle the edge case if the target is greater than the last element
        if target > nums[-1]:
            return len(nums)
        
        # Initialize pointers for binary search
        left, right = 0, len(nums) - 1

        # Binary search loop
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        # If the loop finishes without finding the target,
        # the 'left' pointer indicates the correct position to insert the target.
        return left

# Test the code
def main():
    sol = Solution()
    nums = [1, 3, 5, 6]
    target = 5
    print(sol.searchInsert(nums, target))  # Output: 2

if __name__ == "__main__":
    main()
