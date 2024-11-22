# link: https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        guarded = set()
        wall_set = set(tuple(wall) for wall in walls)
        guard_set = set(tuple(guard) for guard in guards)
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                while nr >= 0 and nr < m and nc >= 0 and nc < n:
                    if (nr, nc) in guard_set or (nr, nc) in wall_set:
                        break
                    else:
                        guarded.add((nr, nc))
                        nr += dr
                        nc += dc

        return m*n - len(walls) - len(guards) - len(guarded)
