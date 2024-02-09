# link: https://leetcode.com/problems/sequential-digits

class Solution:
    def sequentialDigits(self, low: int, high: int) -> list[int]:
        num_str = '123456789'
        width = len(str(low))
        start = int(str(low)[0]) - 1
        res = []

        while width <= 9 and int(num_str[start:start+width]) <= high:
            if int(num_str[start:start+width]) >= low:
                res.append(int(num_str[start:start+width]))
            start += 1
            if start + width - 1 > 8:
                width += 1
                start = 0
        
        return res