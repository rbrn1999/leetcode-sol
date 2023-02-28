# link: https://leetcode.com/problems/edit-distance/

from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1,word2 = word2, word1

        n, m = len(word1), len(word2)
        @cache
        def dfs(i, j):
            if i == n:
                return m - j
            if j == m:
                return n - i

            replace = int(word1[i] != word2[j]) + dfs(i+1, j+1)
            insert = 1 + dfs(i, j+1)
            delete = 1 + dfs(i+1, j)
            return min(replace, insert, delete)

        return dfs(0, 0)

