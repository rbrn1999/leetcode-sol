# link: https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        exp = 31
        res = 0
        while n > 0:
            res += (n % 2) * 2**exp
            n >>= 1
            exp -= 1

        return res
