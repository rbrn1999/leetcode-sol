# link: https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        max_r = ""
        min_r = s[0]
        for c in s:
            if c != '9':
                max_r = c
                break

        max_d = int(''.join(['9' if c == max_r else c for c in s]))
        min_d = int(''.join(['0' if c == min_r else c for c in s]))

        return max_d - min_d

