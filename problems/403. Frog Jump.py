# link: https://leetcode.com/problems/frog-jump/

from functools import cache
class Solution:
    def canCross(self, stones: list[int]) -> bool:
        if stones[1] != 1:
            return False
        n = len(stones)
        stoneIndex = {stone: i for i, stone in enumerate(stones)}
        @cache
        def helper(i=1, k=1):
            if i == n-1:
                return True
            if k-1 > 0 and stones[i] + k - 1 in stoneIndex and helper(stoneIndex[stones[i]+k-1], k-1):
                return True
            if stones[i] + k in stoneIndex and helper(stoneIndex[stones[i]+k], k):
                return True
            if stones[i] + k + 1 in stoneIndex and helper(stoneIndex[stones[i]+k+1], k+1):
                return True
            
            return False

        return helper()