# link: https://leetcode.com/problems/maximize-happiness-of-selected-children/

import heapq
class Solution:
    def maximumHappinessSum(self, happiness: list[int], k: int) -> int:
        # minHeap with size k
        heap = happiness[:k]
        heapq.heapify(heap)

        for i in range(k, len(happiness)):
            heapq.heappushpop(heap, happiness[i])

        maxHeap = [-value for value in heap]
        heapq.heapify(maxHeap)
        decrement = 0
        result = 0
        while maxHeap:
            value = -heapq.heappop(maxHeap)
            if value - decrement <= 0:
                break
            else:
                result += value - decrement
                decrement += 1

        return result
