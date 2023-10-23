# link: https://leetcode.com/problems/power-of-four/
# solution: https://leetcode.com/problems/power-of-four/discuss/80461/Python-one-line-solution-with-explanations
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n != 0 and n&(n-1) == 0 and n&1431655765 == n

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            if n % 4:
                return False
            n //= 4

        return True if n > 0 else False