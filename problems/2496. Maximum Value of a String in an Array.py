# link: https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        ans = 0
        for s in strs:
            hasAlpha = False
            for c in s:
                if c.isalpha():
                    hasAlpha = True
                    break
                else:
                    pass
            if hasAlpha:
                ans = max(ans, len(s))
            else:
                ans = max(ans, int(s))

        return ans
