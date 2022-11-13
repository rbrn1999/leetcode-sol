# link: https://leetcode.com/problems/maximum-69-number/

class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        n = len(s)
        try:
            exp = n - (s.index('6') + 1)
            return num + 3 * 10 ** exp
        except ValueError:
            return num
