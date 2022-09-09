# link: https://leetcode.com/problems/furthest-building-you-can-reach/

import heapq
class Solution:
    def furthestBuilding(self, heights: list[int], bricks: int, ladders: int) -> int:
        diff = [heights[i]-heights[i-1] for i in range(1, len(heights))]
        skips = diff[:ladders]
        heapq.heapify(skips)

        for i in range(ladders+1, len(heights)):
            if diff[i-1] < 0:
                continue
                
            if skips and skips[0]<diff[i-1]:
                bricks -= max(heapq.heappushpop(skips, diff[i-1]), 0)
            else:
                bricks -= diff[i-1]
            
            if bricks < 0:
                return i-1

        return len(heights)-1
