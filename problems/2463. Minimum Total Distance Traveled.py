# link: https://leetcode.com/problems/minimum-total-distance-traveled/

# Bottom-Up
class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        factory = [i for f, count in factory for i in [f] * count]

        distance = [[float('inf')] * (len(factory) + 1) for _ in range(len(robot)+1)]
        distance[0] = [0] * (len(factory) + 1)

        for i in range(len(robot)):
            for j in range(i, len(factory)):
                assign = distance[i][j] + abs(robot[i]-factory[j])
                skip = distance[i+1][j]
                distance[i+1][j+1] = min(assign, skip)

        return distance[-1][-1]

# Bottom-Up Optimized
class Solution:
    def minimumTotalDistance(self, robot: list[int], factory: list[list[int]]) -> int:
        robot.sort()
        factory.sort()
        factory = [i for f, count in factory for i in [f] * count]

        distance = [[float('inf')] * (len(factory) + 1) for _ in range(2)]
        distance[0] = [0] * (len(factory) + 1)

        for i in range(len(robot)):
            for j in range(i, len(factory)):
                assign = distance[0][j] + abs(robot[i]-factory[j])
                skip = distance[1][j]
                distance[1][j+1] = min(assign, skip)
            distance = [distance[1], [float('inf')] * (len(factory) + 1)]

        return distance[0][-1]
