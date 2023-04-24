# link: https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            y = -heapq.heappop(stones)
            x = -heapq.heappop(stones)
            if y > x:
                heapq.heappush(stones, -(y-x))
        
        return -stones[0] if stones else 0


