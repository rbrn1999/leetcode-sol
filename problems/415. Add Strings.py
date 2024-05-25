# link: https://leetcode.com/problems/add-strings/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        maxLength = max(len(num1), len(num2)) + 1
        result = [''] * maxLength
        carry = 0
        for i in range(maxLength):
            val = carry
            if i < len(num1):
                val += int(num1[-1-i])
            if i < len(num2):
                val += int(num2[-1-i])

            carry = val // 10
            val %= 10
            result[-1-i] = str(val)
        
        return ''.join(result) if result[0] != '0' else ''.join(result[1:])
            