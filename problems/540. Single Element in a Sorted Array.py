# link: https://leetcode.com/problems/single-element-in-a-sorted-array/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high-low) // 2 + ((high-low) // 2 + 1) % 2
            if nums[mid] != nums[mid-1] and nums[mid] != nums[mid+1]:
                return nums[mid]
            elif nums[mid] == nums[mid+1]:
                high = mid - 1
            elif nums[mid] == nums[mid-1]:
                low = mid + 1

        return nums[low]

