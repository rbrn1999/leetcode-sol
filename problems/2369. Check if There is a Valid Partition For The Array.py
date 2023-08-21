# link: https://leetcode.com/problems/check-if-there-is-a-valid-partition-for-the-array/

# Top-Down
from functools import cache
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        @cache
        def helper(i) -> bool:
            if i == n:
                return True
            if i + 1 < n and nums[i] == nums[i+1] and helper(i+2):
                return True
            if i + 2 < n and (nums[i]+1 == nums[i+1] and nums[i]+2 == nums[i+2] or nums[i] == nums[i+1] and nums[i] == nums[i+2]) and helper(i+3):
                return True

            return False
        
        return helper(0)

# Bottom-Up
class Solution:
    def validPartition(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False, True, True] # dp[0]: state of dp[i], dp[1]: state of dp[i-1], dp[2]: state of dp[i-2], init at i == 0
        for i in range(1, n):
            temp = i >= 2 and dp[2] and (nums[i] == nums[i-1] and nums[i-1] == nums[i-2] or nums[i] == nums[i-1]+1 and nums[i]-2 == nums[i-2]) \
                    or i >= 1 and dp[1] and nums[i] == nums[i-1]
            dp = [temp, dp[0], dp[1]]
        
        return dp[0]