# link: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/
# solution reference: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/discuss/78334/Python-solution-memoization-dp-288ms
class Solution:
    def longestIncreasingPath(self, matrix: list[list[int]]) -> int:
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                u = dfs(i-1, j) if i>0 and val < matrix[i-1][j] else 0
                d = dfs(i+1, j) if i<M-1 and val < matrix[i+1][j] else 0
                l = dfs(i, j-1) if j>0 and val < matrix[i][j-1] else 0
                r = dfs(i, j+1) if j<N-1 and val < matrix[i][j+1] else 0
                dp[i][j] = 1 + max(u, d, l, r)
                
            return dp[i][j]
        
        M = len(matrix)
        N = len(matrix[0])
        dp = [[None] * N for _ in range(M)]
        for i in range(M):
            for j in range(N):
                dfs(i, j)
        
        return max(map(max, dp))