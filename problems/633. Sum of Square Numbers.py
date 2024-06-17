# link: https://leetcode.com/problems/sum-of-square-numbers/

import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b_square = c - a ** 2
            if b_square == int(math.sqrt(b_square)) ** 2:
                return True

        return False
