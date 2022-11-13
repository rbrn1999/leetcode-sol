# link: https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:

        n = len(s)

        @cache
        def palin(l, r):
            if l < 0 or r >= n or s[l] != s[r]:
                return False
            elif r - l <= 1:
                return True
            else:
                return palin(l+1, r-1)

        @cache
        def dfs(i):
            if i >= n:
                return 0
            count = dfs(i+1)
            if palin(i, i+k-1):
                count = max(count, 1 + dfs(i+k))
            if palin(i, i+k):
                count = max(count, 1 + dfs(i+k+1))
            return count

        return dfs(0)
