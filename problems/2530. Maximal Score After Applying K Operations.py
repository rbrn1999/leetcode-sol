# link: https://leetcode.com/problems/maximal-score-after-applying-k-operations/

import heapq
import math
class Solution:
    def maxKelements(self, nums: list[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)

        score = 0
        for _ in range(k):
            val = -heapq.heappop(heap)
            score += val
            val = math.ceil(val/3)
            heapq.heappush(heap, -val)
        
        return score