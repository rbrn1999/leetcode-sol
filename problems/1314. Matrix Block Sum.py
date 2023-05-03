# link: https://leetcode.com/problems/matrix-block-sum/

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        dp = [[0]*(n+1) for _ in range(m+1)]
        for row in range(m):
            for col in range(n):
               dp[row+1][col+1] = mat[row][col] + dp[row+1][col] + dp[row][col+1] - dp[row][col]

        answer = [[0]*n for _ in range(m)]
        for row in range(m):
            for col in range(n):
                top = max(0, row-k)
                bottom = min(m-1, row+k)
                left = max(0, col-k)
                right = min(n-1, col+k)
                answer[row][col] = dp[bottom+1][right+1] - dp[bottom+1][left] - dp[top][right+1] + dp[top][left]

        return answer

'''
	a   b

	c   d
sum of rectangle (a, b, c, d) => dp[d] - dp[left of c] - dp[top of b] + dp[top-left of a]
(addition rule)
'''

