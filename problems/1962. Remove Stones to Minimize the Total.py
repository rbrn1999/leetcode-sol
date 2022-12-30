# link: https://leetcode.com/problems/remove-stones-to-minimize-the-total
'''
Greedy
Time Complexity: O(n + k*log(N))
Space Complexity: O(n)
'''
import heapq
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxHeap = [-pile for pile in piles]
        heapq.heapify(maxHeap)
        for _ in range(k):
            # num - num // 2 == - (-num//2)
            heapq.heapreplace(maxHeap, maxHeap[0] // 2)
            # equivalent to:
            # pile = -heapq.heappop(maxHeap)
            # pile -= pile // 2
            # heapq.heappush(maxHeap, -pile)

        return -sum(maxHeap)
