# link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/

from functools import cache
class Solution:
    def countMaxOrSubsets(self, nums: list[int]) -> int:
        target = 0
        for num in nums:
            target |= num

        @cache
        def dfs(i: int, value: int, target: int) -> int:
            if i == len(nums):
                return 0
            return int(value | nums[i] == target) + dfs(i+1, value, target) + dfs(i+1, value | nums[i], target)

        return dfs(0, 0, target)
