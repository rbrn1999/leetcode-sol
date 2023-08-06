from functools import cache
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # dp = [[-float('inf')] * len(s2) for _ in range(len(s1))]
        m, n = len(s1), len(s2)
        @cache
        def helper(i, j):
            if i == m and j == n:
                return 0
            if i == m:
                return sum(ord(s2[k]) for k in range(j, n))
            if j == n:
                return sum(ord(s1[k]) for k in range(i, m))
            del_s1 = ord(s1[i]) + helper(i+1, j)
            del_s2 = ord(s2[j]) + helper(i, j+1)
            keep = helper(i+1, j+1) if s1[i] == s2[j] else float('inf')
            return min(del_s1, del_s2, keep)
        
        return helper(0, 0)


print(Solution().minimumDeleteSum("sea", "eat"))