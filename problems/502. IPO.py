# link: https://leetcode.com/problems/ipo/

import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits), reverse=True)
        profitsMaxHeap = []
        for _ in range(k):
            while projects and projects[-1][0] <= w:
                heapq.heappush(profitsMaxHeap, -projects.pop()[1])
            if not profitsMaxHeap:
                return w
            else:
                w += -heapq.heappop(profitsMaxHeap)

        return w

