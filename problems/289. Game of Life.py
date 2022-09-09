# link: https://leetcode.com/problems/game-of-life/

# Any live cell with fewer than two live neighbors dies as if caused by under-population.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any live cell with more than three live neighbors dies, as if by over-population.
# Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

from typing import List
from copy import deepcopy
class Solution:

    # 0,2 are "dead", and "dead->live"
    # 1,3 are "live", and "live->dead"
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        def neighbors(i: int, j: int) -> int:
            return sum([board[x][y]%2 for x in range(i-1,i+2) for y in range(j-1,j+2) if 0 <= x < m and 0<= y < n]) - board[i][j]
        

        for i in range(m):
            for j in range(n):
                nCount = neighbors(i, j)
                print(f'board[{i}][{j}]: {board[i][j]} {nCount}')
                if board[i][j] == 0 and nCount == 3: #revive dead cell
                    board[i][j] = 2
                    print('live')
                elif board[i][j] == 1 and (nCount < 2 or nCount > 3):
                    board[i][j] = 3
                    print('die')

        for i in range(m):
            for j in range(n):
                if board[i][j] == 3:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1



board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
b = deepcopy(board)
Solution().gameOfLife(board=board)
print(b)
print(board)