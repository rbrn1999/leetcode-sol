# link: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
# solution reference: https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/452434/

'''
BFS
Time Complexity: O(m*n*k)
Space Complexity: O(m*n*k) (not sure)
'''

from collections import deque
class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        curLvl = deque([(0, 0, k)])
        nxtLvl = deque()
        seen = set(curLvl[0])
        
        step = 0
        
        while curLvl:
            row, col, r = curLvl.popleft()
            if row == m-1 and col == n-1:
                return step
            for offset_r, offset_c in dirs:
                nRow, nCol = row + offset_r, col + offset_c
                if nRow < 0 or nCol < 0 or nRow >= m or nCol >= n:
                    continue
                nR =  r - grid[nRow][nCol]
                state = (nRow, nCol, nR)
                if nR >= 0 and state not in seen:
                    seen.add(state)
                    nxtLvl.append(state)
                    
            if not curLvl:
                curLvl, nxtLvl = nxtLvl, deque()
                step += 1
            
        return -1