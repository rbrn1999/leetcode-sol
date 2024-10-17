# link: https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

# Heap
import heapq
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        groups = 1
        ends = []

        for l, r in intervals:
            while ends and ends[0] < l:
                heapq.heappop(ends)

            heapq.heappush(ends, r)
            groups = max(groups, len(ends))

        return groups


# Line Sweep
class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        max_right = max(right for _, right in intervals)
        min_left = min(left for left, _ in intervals)
        points = [0] * (max_right-min_left+2)
        current_intervals = 0
        groups = 0

        for l, r in intervals:
            points[l-min_left] += 1
            points[r+1-min_left] -= 1

        for point in points:
            current_intervals += point
            groups = max(groups, current_intervals)

        return groups
