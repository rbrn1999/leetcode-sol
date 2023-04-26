# link: https://leetcode.com/problems/sum-multiples/

class Solution:
    def sumOfMultiples(self, n: int) -> int:
        def sumOfMul(num: int) -> int:
            # (low + high) * (count) / 2
            return num * (1 + n // num) * (n // num) // 2

        return sumOfMul(3) + sumOfMul(5) + sumOfMul(7) - (sumOfMul(3*5)+sumOfMul(3*7)+sumOfMul(5*7)) + sumOfMul(3*5*7)

