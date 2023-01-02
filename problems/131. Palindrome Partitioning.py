# link: https://leetcode.com/problems/palindrome-partitioning/

from functools import cache
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        n = len(s)
        arr = []
        @cache
        def isPalindrome(start, end):
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def dfs(i):
            if i == n:
                result.append(arr.copy())
                return
            for j in range(i, n):
                if isPalindrome(i, j):
                    arr.append(s[i:j+1])
                    dfs(j+1)
                    arr.pop()

        dfs(0)
        return result

