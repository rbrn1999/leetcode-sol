# link: https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        if n == 0:
            return 0
        
        e_5 = 0
        while n:
            e_5 += n // 5
            n //= 5
        
        return e_5