# link: https://leetcode.com/problems/sum-of-square-numbers/

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

