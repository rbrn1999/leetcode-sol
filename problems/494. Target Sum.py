# link: https://leetcode.com/problems/target-sum/
'''
Time Complexity: O(t⋅n)
Space Complexity: O(t⋅n)
t refers to to sum of nums array
(the sum will be in range of [-t ~ +t])
'''

from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(i=0, target=target):
            if i == n:
                return 1 if (target == 0) else 0

            return dfs(i+1, target-nums[i]) + dfs(i+1, target+nums[i])

        return dfs()
