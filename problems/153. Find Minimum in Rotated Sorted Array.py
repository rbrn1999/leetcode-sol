#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
# link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

# @lc code=start
class Solution:
    def findMin(self, nums: list[int]) -> int:
        def bsearch(low, high):
            if nums[low] < nums[high]: # sorted (no rotation in range)
                return nums[low]
            if low == high:
                return nums[low]
            if high-low == 1:
                return min(nums[low], nums[high])

            mid = low + (high-low)//2
            if nums[mid] < nums[low]: # right portion
                return bsearch(low, mid)
            else:                     # left portion
                return bsearch(mid+1, high)
        
        return bsearch(0, len(nums)-1)

# @lc code=end

