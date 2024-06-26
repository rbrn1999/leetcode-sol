# link: https://leetcode.com/problems/length-of-last-word/

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        r = len(s)-1
        while s[r] == ' ':
            r -= 1

        l = r
        while l > 0 and s[l-1] != ' ':
            l -= 1

        return r - l + 1
