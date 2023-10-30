# link: https://leetcode.com/problems/minimum-increment-operations-to-make-array-beautiful/

# Top-Down
from functools import cache
class Solution:
    def minIncrementOperations(self, nums: list[int], k: int) -> int:
        @cache
        def dfs(i):
            if i >= len(nums):
                return 0
            if nums[i] >= k:
                return dfs(i+3)
            if nums[i-1] >= k:
                return dfs(i+2)
            if nums[i-2] >= k:
                return dfs(i+1)
            
            ops = (k-nums[i]) + dfs(i+3)
            if nums[i-1] > nums[i]:
                ops = min(ops, (k-nums[i-1] + dfs(i+2)))
            if nums[i-2] > nums[i-1]:
                ops = min(ops, (k-nums[i-2] + dfs(i+1)))
            return ops
        
        return dfs(2)
            