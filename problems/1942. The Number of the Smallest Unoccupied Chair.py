# link: https://leetcode.com/problems/the-number-of-the-smallest-unoccupied-chair/

import heapq
class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:
        targetTime = times[targetFriend][0]
        times.sort()
        seats = list(range(len(times)))
        ends = []
        for arrival, leave in times:
            while ends and ends[0][0] <= arrival:
                _, seat = heapq.heappop(ends)
                heapq.heappush(seats, seat)

            seat = heapq.heappop(seats)
            if arrival == targetTime:
                return seat

            heapq.heappush(ends, (leave, seat))

        return -1
