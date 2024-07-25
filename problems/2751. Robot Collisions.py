# link: https://leetcode.com/problems/robot-collisions/

class Solution:
    def survivedRobotsHealths(self, positions: list[int], healths: list[int], directions: str) -> list[int]:
        n = len(positions)
        robots = sorted((positions[i], directions[i], healths[i], i) for i in range(n))
        robots_right = []
        robots_left = []

        for _, direction, health, i in robots:
            if direction == 'R':
                robots_right.append([health, i])
            else:
                while robots_right and robots_right[-1][0] < health:
                    robots_right.pop()
                    health -= 1

                if not robots_right:
                    robots_left.append([health, i])
                elif robots_right[-1][0] == health:
                    robots_right.pop()
                else:
                    robots_right[-1][0] -= 1

        final_healths = [0] * n
        for health, i in robots_left:
            final_healths[i] = health
        for health, i in robots_right:
            final_healths[i] = health

        result = [final_healths[i] for i in range(n) if final_healths[i] > 0]

        return result
