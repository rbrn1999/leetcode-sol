# link: https://leetcode.com/problems/count-number-of-homogenous-substrings/

class Solution:
    def countHomogenous(self, s: str) -> int:
        s += '_'
        count = 0
        l = 0
        for r in range(1, len(s)):
            if s[r] != s[l]:
                n = r - l
                count += (n * (1 + n) // 2) % int(1E9 + 7)
                l = r

        return count % int(1E9 + 7)
