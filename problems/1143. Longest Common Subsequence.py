# link: https://leetcode.com/problems/longest-common-subsequence/

'''
top-bottom dynamic programming
Time Complexity: O(m*n)
Space Complexity: O(m*n)
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        def helper(i, j):
            if i < 0 or j < 0:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            length = 0
            if text1[i] == text2[j]:
                length = helper(i-1, j-1) + 1
            else:
                length = max(helper(i-1, j), helper(i, j-1)) # two different routes

            memo[(i, j)] = length
            return length

        return helper(m-1, n-1)


# bottom-up recursion solution
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        memo = {}
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            length = 0
            if text1[i] == text2[j]:
                length = 1 + dfs(i+1, j+1)
            else:
                length = max(dfs(i+1, j), dfs(i, j+1))

            memo[(i, j)] = length
            return length

        return dfs(0, 0)

# Bottom-Up iterative
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)] # dp[i][j]: max subsequence of text1[:i], text2[:j]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        
        return dp[m][n]
    
# Bottom-Up optimized space
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text2) > len(text1):
            text1, text2 = text2, text1
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(2)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[1][j+1] = dp[0][j] + 1
                else:
                    dp[1][j+1] = max(dp[1][j], dp[0][j+1])
            dp = [dp[1], [0]*(n+1)]
        
        return dp[0][n]