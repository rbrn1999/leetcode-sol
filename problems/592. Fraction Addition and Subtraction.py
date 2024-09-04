# link: https://leetcode.com/problems/fraction-addition-and-subtraction/

import math
class Solution:
    def fractionAddition(self, expression: str) -> str:
        a = 0
        b = 1
        # a/b

        i = 0
        while i < len(expression):
            sign = 1 if expression[i] != '-' else -1
            j = i + int(not expression[i].isdigit())
            c = 0
            while expression[j] != '/':
                c = c * 10 + int(expression[j])
                j += 1
            j += 1
            d = 0
            while j < len(expression) and expression[j].isdigit():
                d = d * 10 + int(expression[j])
                j += 1

            gcd = math.gcd(b, d)
            a = sign * (c * b // gcd) + a * d // gcd
            b = b * d // gcd

            gcd = math.gcd(a, b)
            a //= gcd
            b //= gcd

            i = j
        
        return f"{a}/{b}"