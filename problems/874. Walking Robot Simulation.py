# link: https://leetcode.com/problems/walking-robot-simulation/

class Solution:
    def robotSim(self, commands: list[int], obstacles: list[list[int]]) -> int:
        obstacles_set = set(tuple(obstacle) for obstacle in obstacles)
        max_distance = 0
        row, col = 0, 0
        dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
        d = 0
        for value in commands:
            if value == -1:
                d = (d - 1 + 4) % 4
            elif value == -2:
                d = (d + 1) % 4
            else:
                for _ in range(value):
                    row += dirs[d][0]
                    col += dirs[d][1]
                    if (row, col) in obstacles_set:
                        row -= dirs[d][0]
                        col -= dirs[d][1]
                        break

            max_distance = max(max_distance, row ** 2 + col ** 2)

        return max_distance
