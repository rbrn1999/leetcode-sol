# link: https://leetcode.com/problems/find-valid-matrix-given-row-and-column-sums/

# Greedy (reference: https://youtu.be/Ks6fGnXkHPg)
class Solution:
    def restoreMatrix(self, rowSum: list[int], colSum: list[int]) -> list[list[int]]:
        # fill each cell with the maximum number possible, then shift the extra value to the next cell

        m, n = len(rowSum), len(colSum)
        matrix = [[0] * n for _ in range(m)]

        for row in range(m):
            matrix[row][0] = rowSum[row]
        
        for col in range(n):
            cur_col_sum = sum(matrix[row][col] for row in range(m))

            row = 0
            while cur_col_sum > colSum[col]:
                diff = cur_col_sum - colSum[col]
                max_shift = min(matrix[row][col], diff)

                matrix[row][col] -= max_shift
                matrix[row][col+1] += max_shift
                cur_col_sum -= max_shift
                row += 1
        
        return matrix
        

# apporach with hint
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