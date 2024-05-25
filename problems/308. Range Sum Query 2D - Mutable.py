# link: https://leetcode.com/problems/range-sum-query-2d-mutable/

import itertools

class NumMatrix:

    def __init__(self, matrix: list[list[int]]):
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        self.preSum = [[0] * (self.n+1) for _ in range(self.m+1)] # sum of (0, 0) to (row-1, col-1) rectangle
        for row, col in itertools.product(range(self.m), range(self.n)):
            self.preSum[row+1][col+1] = matrix[row][col] + self.preSum[row][col+1] + self.preSum[row+1][col] - self.preSum[row][col]

    def update(self, row: int, col: int, val: int) -> None:
        self.matrix[row][col] = val
        for row, col in itertools.product(range(row, self.m), range(col, self.n)):
            self.preSum[row+1][col+1] = self.matrix[row][col] + self.preSum[row][col+1] + self.preSum[row+1][col] - self.preSum[row][col]        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.preSum[row2+1][col2+1] - self.preSum[row1][col2+1] - self.preSum[row2+1][col1] + self.preSum[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)