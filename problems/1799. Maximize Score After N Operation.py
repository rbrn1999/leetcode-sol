# link: https://leetcode.com/problems/maximize-score-after-n-operations/

import math
from functools import cache
class Solution:
    def maxScore(self, nums: list[int]) -> int:
        n = len(nums) // 2
        @cache
        def gcd(a, b):
            return math.gcd(a, b)

        @cache
        def dfs(i: int=1, mask: int=0) -> int:
            score = 0
            for first in range(n*2-1):
                for second in range(first+1, n*2):
                    newMask = 1 << first | 1 << second
                    if mask & newMask == 0:
                        score = max(score, i * gcd(nums[first], nums[second]) + dfs(i+1, mask | newMask))
            return score
        
        return dfs()