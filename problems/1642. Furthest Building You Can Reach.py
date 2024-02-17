# link: https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        diff_maxHeap = []

        for i in range(1, len(heights)):
            if heights[i] <= heights[i-1]:
                continue
            bricks -= heights[i] - heights[i-1]
            heapq.heappush(diff_maxHeap, -(heights[i] - heights[i-1]))
            if bricks < 0:
                if ladders == 0:
                    return i-1
                bricks += -(heapq.heappop(diff_maxHeap))
                ladders -= 1
        
        return len(heights) - 1
