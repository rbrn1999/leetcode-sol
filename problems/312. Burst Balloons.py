# link: https://leetcode.com/problems/burst-balloons/

from functools import cache
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # dp[l][r]: l: left bound index, r: right bound index -> maximum of subarray nums[l:r+1]
        @cache
        def dfs(l, r):
            max_coins = 0
            for i in range(l, r+1):
                # pop the left subarray and right subarray before popping nums[i]
                left_bound = nums[l-1] if l > 0 else 1
                right_bound = nums[r+1] if r < len(nums) - 1 else 1
                coins = left_bound * nums[i] * right_bound
                coins += dfs(l, i-1) + dfs(i+1, r)
                max_coins = max(max_coins, coins)
            
            return max_coins
        
        return dfs(0, len(nums)-1)
        