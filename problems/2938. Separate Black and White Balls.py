# link: https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        l = 0
        steps = 0
        for r in range(len(s)):
            if s[r] == '0':
                steps += r - l
                l += 1

        return steps
