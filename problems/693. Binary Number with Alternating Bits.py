# link: https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = n % 2
        n //= 2
        while n > 0:
            if prev == n%2:
                return False
            else:
                n //= 2
                prev = 0 if prev else 1
        return True
