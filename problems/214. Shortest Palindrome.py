# link: https://leetcode.com/problems/shortest-palindrome/

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        def check(l: int, r: int):
            while l >= 0 and r < n:
                if s[l] != s[r]:
                    return False
                l -= 1
                r += 1
            return l < 0

        n = len(s)
        for i in range(n//2 - (n+1)%2, -1, -1):
            if check(i, i+1):
                return s[i+1:][::-1] + s[i+1:]
            if check(i, i):
                return s[i+1:][::-1] + s[i] + s[i+1:]
        
        return s[::-1] + s