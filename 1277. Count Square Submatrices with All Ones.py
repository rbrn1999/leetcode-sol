# link: https://leetcode.com/problems/count-square-submatrices-with-all-ones/
# Example 1:

# Input: matrix =
# [
#   [0,1,1,1],
#   [1,1,1,1],
#   [0,1,1,1]
# ]
# Output: 15
# Explanation: 
# There are 10 squares of side 1.
# There are 4 squares of side 2.
# There is  1 square of side 3.
# Total number of squares = 10 + 4 + 1 = 15.
# Example 2:

# Input: matrix = 
# [
#   [1,0,1],
#   [1,1,0],
#   [1,1,0]
# ]
# Output: 7
# Explanation: 
# There are 6 squares of side 1.  
# There is 1 square of side 2. 
# Total number of squares = 6 + 1 = 7.
 

# Constraints:

# 1 <= arr.length <= 300
# 1 <= arr[0].length <= 300
# 0 <= arr[i][j] <= 1
from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        def isSquare(x, y, side):
            if x + side > m or y + side > n:
                return False
            for i in range(x, x+side):
                for j in range(y, y+side):
                    if matrix[i][j] == 0:
                        return False
            return True
        
        m = len(matrix)
        n = len(matrix[0])
        total = 0
        
        for i in range(m):
            for j in range(n):
                side = 1
                while isSquare(i, j, side):
                    # print(f'{i}, {j} ,{side}')
                    total += 1
                    side += 1
        return total

    # dp solution
    # def countSquares(self, A: List[List[int]]) -> int:
    #       # start at index 1 because the 3 edge element can't form squares larger than 1*1
    #       # dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
    #       # dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.
    #     for i in range(1, len(A)):
    #         for j in range(1, len(A[0])):
    #             A[i][j] = (min(A[i - 1][j - 1], A[i - 1][j], A[i][j - 1]) + 1 if A[i][j] == 1 else 0)
    #     return sum(map(sum, A))

matrix = [
  [1,0,1],
  [1,1,0],
  [1,1,0]
]

print(Solution().countSquares(matrix))