# link: https://leetcode.com/problems/buy-two-chocolates/

import heapq
class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        maxHeap = []
        for price in prices:
            heapq.heappush(maxHeap, -price)
            while len(maxHeap) > 2:
                heapq.heappop(maxHeap)
        
        return money - (-1) * sum(maxHeap) if -1 * sum(maxHeap) <= money else money