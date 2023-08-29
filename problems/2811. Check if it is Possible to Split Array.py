# link: https://leetcode.com/problems/check-if-it-is-possible-to-split-array/

class Solution:
    def canSplitArray(self, nums: list[int], m: int) -> bool:
        if len(nums) <= 2: # edge case: [x, y], x+y < m
            return True
        for i in range(len(nums)-1):
            if nums[i] + nums[i+1] >= m:
                return True
        
        return False