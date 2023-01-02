# link: https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False
        memo = {}
        def dfs(ptr1=0, ptr2=0):
            if (ptr1, ptr2) in memo:
                return memo[(ptr1, ptr2)]
            
            if ptr1 == m and ptr2 == n:
                memo[(ptr1, ptr2)] = True
                return True

            ptr3 = ptr1 + ptr2
            if ptr1 < m and s1[ptr1] == s3[ptr3] and dfs(ptr1+1, ptr2):
                memo[(ptr1, ptr2)] = True
                return True
            if ptr2 < n and s2[ptr2] == s3[ptr3] and dfs(ptr1, ptr2+1):
                memo[(ptr1, ptr2)] = True
                return True

            memo[(ptr1, ptr2)] = False
            return False

        return dfs()
