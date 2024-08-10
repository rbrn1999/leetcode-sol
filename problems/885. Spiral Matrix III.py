# link: https://leetcode.com/problems/spiral-matrix-iii/

class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> list[list[int]]:
        path = []
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        straight = 1
        rounds = 0
        k = 0
        d = 0


        r, c = rStart, cStart

        while len(path) < rows * cols:
            if r >= 0 and r < rows and c >= 0 and c < cols:
                path.append([r, c])
            
            r, c = r+dirs[d][0], c+dirs[d][1]
            k += 1

            if k == straight:
                k = 0
                d = (d+1) % len(dirs)
                rounds += 1
                if rounds == 2:
                    rounds = 0
                    straight += 1
        
        return path
            
