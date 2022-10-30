# link: https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur = nums[0]
        maxSum = cur
        for num in nums[1:]:
            cur = max(cur + num, num)
            maxSum = max(maxSum, cur)
        return maxSum
    