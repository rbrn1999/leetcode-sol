# link: https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = []
        while n>0:
            digits.append(n%10)
            n //= 10
        p = 1
        for d in digits:
            p *= d

        return p - sum(digits)
