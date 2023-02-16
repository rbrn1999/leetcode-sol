# link: https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        a = a[::-1]
        b = b[::-1]

        carry = 0
        i = 0
        while i < len(a) or i < len(b) or carry > 0:
            sum_val = carry
            sum_val += int(a[i]) if i < len(a) else 0
            sum_val += int(b[i]) if i < len(b) else 0

            result.append(sum_val % 2)
            carry = sum_val // 2

            i += 1

        if len(result) > 1 and result[-1] == 0:
            result.pop()

        return ''.join(str(digit) for digit in result[::-1])
