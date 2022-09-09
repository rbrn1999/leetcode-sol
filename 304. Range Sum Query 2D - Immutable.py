# link: https://leetcode.com/problems/range-sum-query-2d-immutable/

# LeetCode solution: https://leetcode.com/problems/range-sum-query-2d-immutable/solution/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.dp = [[0]*(n+1) for _ in range(m+1)] # dp[i][j]: sum of rectangle matrix[0][0] to matrix[i-1][j-1]

        for row in range(m):
            for col in range(n):
                self.dp[row+1][col+1] = self.dp[row][col+1] + self.dp[row+1][col] - self.dp[row][col] + matrix[row][col]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.dp[row2+1][col2+1] - self.dp[row2+1][col1] - self.dp[row1][col2+1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
