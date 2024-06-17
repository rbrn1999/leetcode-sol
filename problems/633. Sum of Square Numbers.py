# link: https://leetcode.com/problems/sum-of-square-numbers/

# sqrt
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(int(math.sqrt(c))+1):
            b_square = c - a ** 2
            if b_square == int(math.sqrt(b_square)) ** 2:
                return True

        return False

# 2-sum
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_c = int(math.sqrt(c))
        if sqrt_c ** 2 == c:
            return True

        nums = [num ** 2 for num in range(1, int(math.sqrt(c))+1)]
        s = set()
        for num in nums:
            s.add(c - num)
            if num in s:
                return True

        return False
