# link: https://leetcode.com/problems/soup-servings/

from math import ceil
from functools import cache
class Solution:
    def soupServings(self, n: int) -> float:
        n = ceil(n / 25)

        @cache
        def probability(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1
            if b <= 0:
                return 0
            return (probability(a-1, b-3) + probability(a-2, b-2) + probability(a-3, b-1) + probability(a-4, b)) / 4
        
        # for i in range(1, n+1):
        #     if 1 - probability(i, i) < 1e-5:
        #         return 1
        if n >= 192:
            return 1.0
        
        return probability(n, n)
