# link: https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        digits[-1] += 1
        i = n - 1
        while digits[i] > 9 and i > 0:
            digits[i-1] += 1
            digits[i] %= 10
            i -= 1
        if digits[0] > 9:
            digits[0] %= 10
            digits.insert(0, 1)

        return digits

