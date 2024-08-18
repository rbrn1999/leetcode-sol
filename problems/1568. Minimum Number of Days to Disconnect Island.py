# link: https://leetcode.com/problems/minimum-number-of-days-to-disconnect-island/


# Brute Force
import itertools
class Solution:
    def minDays(self, grid: list[list[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        def dfs(r: int, c: int, seen: set) -> None:
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == 0 or (r, c) in seen:
                return

            seen.add((r, c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc, seen)

        seen = set()
        for r, c in itertools.product(range(ROW), range(COL)):
            if grid[r][c] == 0:
                continue
            elif seen and (r, c) not in seen:
                return 0
            else:
                dfs(r, c, seen)

        if not seen:
            return 0
        if len(seen) <= 2:
            return len(seen)

        for r, c in seen:
            grid[r][c] = 0
            visited = set()
            for dr, dc in dirs:
                if (r+dr, c+dc) in seen:
                    dfs(r+dr, c+dc, visited)
                    break

            if len(visited) < len(seen)-1:
                return 1

            grid[r][c] = 1

        return 2
