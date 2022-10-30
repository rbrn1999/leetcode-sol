# link: https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/

class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        digitSum = 0
        digits = []
        cur = n
        while n > 0:
            digitSum += n % 10
            digits.append(n % 10)
            n //= 10
        
        digits.append(0)
        
        exp = 0
        res = 0
        
        while digitSum > target:
            if digits[exp] == 0:
                exp += 1
                continue
            res += (10 - digits[exp]) * (10**exp)
            digitSum -= (digits[exp] - 1)
            digits[exp+1] += 1
            exp += 1
            while digits[exp] == 10:
                digitSum -= 9
                digits[exp+1] += 1
                exp += 1
                
        return res