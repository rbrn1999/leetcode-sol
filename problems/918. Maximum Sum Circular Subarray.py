# link: https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSub = float('-inf')
        curSum = 0
        for num in nums:
            curSum = num + max(curSum, 0)
            maxSub = max(maxSub, curSum)

        minSub = float('inf')
        curSum = 0
        for num in nums:
            curSum = num + min(curSum, 0)
            minSub = min(minSub, curSum)

        if all(num < 0 for num in nums):
            return maxSub
        else:
            return max(maxSub, sum(nums) - minSub)

