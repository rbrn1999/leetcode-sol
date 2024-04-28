# link: https://leetcode.com/problems/regular-expression-matching/
from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def dfs(i: int=len(s)-1, j: int=len(p)-1) -> bool:
            if i == -1 and j == -1:
                return True
            if j == -1:
                return False
            if i == -1:
                while j > 0 and p[j] == '*':
                    j -= 2
                return j == -1

            if p[j] == '*':
                c = p[j-1]
                if c != s[i] and c != '.':
                    return dfs(i, j-2)
                else:
                    return dfs(i-1, j) or dfs(i, j-2)
            elif p[j] == '.' or s[i] == p[j]:
                return dfs(i-1, j-1)
            else:
                return False

        return dfs()
