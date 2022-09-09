# link: https://leetcode.com/problems/divide-two-integers/
# solution: https://leetcode.com/problems/divide-two-integers/discuss/13407/C%2B%2B-bit-manipulations

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if divisor == -1 and dividend == -(2**31):
            return 2**31 - 1
        sign = 1 if (dividend>0) == (divisor>0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            mul = 1
            temp = divisor
            while (temp << 1) <= dividend:
                temp <<= 1
                mul <<= 1
            dividend -= temp
            result += mul

        return sign * result
