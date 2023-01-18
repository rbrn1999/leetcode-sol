# link: https://leetcode.com/problems/maximum-sum-circular-subarray/
# Kadane's algorithm

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

# 2023/01/18
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)

        maxSub = float('-inf')
        curSum = 0
        for i in range(n):
            curSum += nums[i]
            maxSub = max(maxSub, curSum)
            if curSum < 0:
                curSum = 0

        minSub = float('inf')
        curSum = 0
        temp_l = l = r = 0
        for i in range(n):
            curSum += nums[i]
            if curSum < minSub:
                l = temp_l
                r = i
                minSub = curSum
            if curSum > 0:
                temp_l = i
                curSum = 0

        return max(maxSub, (sum(nums) - minSub) if r-l+1 < n else float('-inf'))
