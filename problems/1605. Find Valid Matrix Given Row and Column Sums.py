# link: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        while True:
            isRow = True
            minVal = float('inf')
            index = None

            for i, row in enumerate(rowSum):
                if row == 0:
                    continue
                if row < minVal:
                    minVal = row
                    index = i
            
            for i, col in enumerate(colSum):
                if col == 0:
                    continue
                if col < minVal:
                    minVal = col
                    index = i
                    isRow = False
            
            if index is None:
                break
            
            if isRow:
                col = 0
                while col < len(colSum):
                    if matrix[index][col] == 0 and colSum[col] >= minVal:
                        break
                    else:
                        col += 1
                matrix[index][col] = minVal
                rowSum[index] -= minVal
                colSum[col] -= minVal
            else:
                row = 0
                while row < len(rowSum):
                    if matrix[row][index] == 0 and rowSum[row] >= minVal:
                        break
                    else:
                        row += 1
                matrix[row][index] = minVal
                rowSum[row] -= minVal
                colSum[index] -= minVal
        
        return matrix