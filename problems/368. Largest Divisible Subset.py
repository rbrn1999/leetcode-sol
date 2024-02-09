# link: https://leetcode.com/problems/largest-divisible-subset/

class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        n = len(nums)
        nums.sort()
        dp = []
        for i in range(n):
            cur = [nums[i]]
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) + 1 > len(cur):
                    cur = dp[j] + [nums[i]]
            dp.append(cur)
        
        res = []
        for l in dp:
            if len(l) > len(res):
                res = l

        return res