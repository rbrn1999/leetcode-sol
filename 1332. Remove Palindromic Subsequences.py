# link: https://leetcode.com/problems/remove-palindromic-subsequences/

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        # worst case: remove all 'a' -> remove all 'b' = 2
        n = len(s)
        if s[:n//2] == s[-1:-(n//2+1):-1]:
            return 1
        else:
            return 2
