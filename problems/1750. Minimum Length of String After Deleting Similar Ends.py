# link: https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        l = 0
        r = len(s) - 1

        while l < r and s[l] == s[r]:
            while l+1 < r and s[l+1] == s[l]:
                l += 1
            while l < r-1 and s[r-1] == s[r]:
                r -= 1
            
            l += 1
            r -= 1
        
        return r - l + 1