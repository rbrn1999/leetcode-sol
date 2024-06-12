# link: https://leetcode.com/problems/sort-colors/

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0
        m = 0
        r = len(nums) - 1
        while m <= r:
            if nums[m] == 0:
                nums[l], nums[m] = nums[m], nums[l]
                l += 1
                m = max(l, m)
            elif nums[m] == 1:
                m += 1
            else:
                nums[r], nums[m] = nums[m], nums[r]
                r -= 1
