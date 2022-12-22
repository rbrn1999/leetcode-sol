# link: https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        sign = 1 if n >= 0 else -1
        n = abs(n)
        result = 1.0
        for _ in range(n):
            result *= x
        
        if sign == -1:
            result = 1 / result
        
        return result