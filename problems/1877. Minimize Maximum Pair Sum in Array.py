# link: https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        curMax = -float('inf')
        n = len(nums)
        for i in range(n//2):
            curMax = max(curMax, nums[i] + nums[n-1-i])
        
        return curMax

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[i] + nums[-1-i] for i in range(len(nums)//2))