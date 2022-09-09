# link: https://leetcode.com/problems/spiral-matrix/

from enum import Enum
from typing import List

class Direction(Enum):
     RIGHT = 0
     DOWN = 1
     LEFT = 2
     UP = 3

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        dir = Direction.RIGHT
        i, j = 0, -1
        cur = 1
        while cur <= n**2:
            if dir == Direction.RIGHT:
                x, y = 0, 1
            elif dir == Direction.DOWN:
                x, y = 1, 0
            elif dir == Direction.LEFT:
                x, y = 0, -1
            elif dir == Direction.UP:
                x, y = -1, 0

            # print(f'i: {i+x}, j: {j+y}, {i+x < n and j+y < n}, {i+x >= 0 and j+y >= 0}')
            if i+x < n and j+y < n and i+x >= 0 and j+y >= 0 and result[i+x][j+y] == 0:
                i += x
                j += y
                result[i][j] = cur
                # print(cur)
                cur += 1
            else:
                # sleep(5)
                dir = Direction((dir.value+1)%4)
                # print(dir)
            
        return result

matrix = Solution().generateMatrix(20)
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))
