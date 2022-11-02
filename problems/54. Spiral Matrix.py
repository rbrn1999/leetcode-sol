# link: https://leetcode.com/problems/spiral-matrix/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        visited = set()
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        pos = (0, 0)
        dir_ind = 0
        res = []
        while len(res) < m*n:
            res.append(matrix[pos[0]][pos[1]])
            visited.add(pos)
            nPos = (pos[0]+dirs[dir_ind][0],  pos[1]+dirs[dir_ind][1])
            if nPos in visited or nPos[0] < 0 or nPos[0] >= m or nPos[1] < 0 or nPos[1] >= n:
                dir_ind = (dir_ind + 1) % len(dirs)
                nPos = (pos[0]+dirs[dir_ind][0],  pos[1]+dirs[dir_ind][1])
                if nPos in visited or nPos[0] < 0 or nPos[0] >= m or nPos[1] < 0 or nPos[1] > n:
                    break
            pos = nPos

        return res
