# link: https://leetcode.com/problems/palindromic-substrings/
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        n = len(s)
        def helper(l, r): # expand from the middle of palindromic string
            nonlocal res
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
                res += 1
        
        for i in range(n):
            helper(i, i)
            helper(i, i+1)
            
        return res