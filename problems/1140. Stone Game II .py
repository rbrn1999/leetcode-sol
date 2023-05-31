# link: https://leetcode.com/problems/stone-game-ii/

from functools import cache
class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        @cache
        def helper(p: int=0, i: int=0, m: int=1): # p=0: Alice, p=1: Bob, return: Alice's score
            if i == n:
                return 0
            
            if p == 0:
                value = 0
                preSum = 0
                for x in range(1, min(n-i, 2*m)+1):
                    preSum += piles[i+x-1]
                    value = max(value, helper(1, i+x, max(x, m)) + preSum)
                return value
            else:
                value = float('inf')
                for x in range(1, min(n-i, 2*m)+1):
                    value = min(value, helper(0, i+x, max(x, m)))
                return value
        
        return helper()
                
