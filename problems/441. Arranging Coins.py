# link: https://leetcode.com/problems/arranging-coins/

import math
class Solution:
    def arrangeCoins(self, n: int) -> int:
        # n: (1+2+3+...+n) = (1 + stairs) * stairs / 2
        # (stairs + 1) * stairs <= 2 * n
        # (stairs + 1/2)^2 - 1/4 <= 2 * n
        
        return int(math.sqrt(2*n + 1/4) - 1/2)